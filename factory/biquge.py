#!/usr/bin/python
#coding:utf-8

import random
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import hashlib
import time

from config_old import source
from config_old import header
from source_template import SourceTemplate
from models.book import Book
from models.book_source import Book_Source
from models.chapter import Chapter

class biquge(SourceTemplate):
	def __init__(self, url):
		self.url = url

	##
	# 抓取小说正文
	#
	def article(self):
		url = self.url
		per_artitle_limit_page = 3;
		title=''
		content=''
		for i in range(1, per_artitle_limit_page):
			if i==1:
				part_url = ''
			else:
				part_url = '_%s'%i

			bs = self.get_request(url.replace('.html',part_url + '.html'))

			# title
			if len(title)<=0:
				title = bs.find('li','active').get_text()#re.findall(title_re, _tempbook)[0]

			
			content_tag = bs.find('div', id='htmlContent')
			if content_tag==None:
				break
			
			next_tag = content_tag.find('p', 'text-danger')
			if next_tag!=None:
				next_tag.clear()
			_ = content_tag.get_text()
			content += _

		return {'title': title, 'content': self.filter(content)}

	##
	# 第二步
	# 抓取简介，返回结构体
	# 标题：知否？知否？应是绿肥红瘦
	# 作者：关心则乱
	# 分类：都市言情
	# 字数：200万
	# 阅读数：2w+
	# 状态：连载中、完结
	# 封面：url
	# 简介：赵丽颖、冯绍峰主演电视剧《知否？知否？应是绿肥红瘦》原著，该剧由正午阳光影业出品，侯鸿亮任制片人，2017年9月6日开机。宅斗翘楚、古言大神关心则乱，手把手传授你实用的古代生存指南。一个消极怠工的古代庶女，生活如此艰难，何必卖力奋斗。古代贵族女子的人生基调是由家族决定的，还流行株连，一个飞来横祸就会彻底遭殃，要活好活顺活出尊严，明兰表示，鸭梨很大。古代太危险了，咱们还是睡死算了。
	# 
	def summary(self):
		_index = 0
		for book_source in Book_Source.select(Book_Source).join(Book, 'INNER', Book.id == Book_Source.bid).where((Book.status != '已完成') & (Book_Source.bid >= _index) & (Book_Source.source == self.__class__.__name__)):
			url = book_source.url
			book = Book.select().where(Book.id == book_source.bid)[0]
			print('start book(%d, %s)'%(book.id, book.title))
			# book={'title':'', 'author':'', 'category':'', 'words':'', 'readers':'', 'status':'', 'cover_img':'', 'summary':''}
			_bookDict = {}

			bs = self.get_request(url)
			
			title_tag = bs.find('h1', 'bookTitle')
			if title_tag!=None:
				_bookDict['title'] = title_tag.get_text()

			book_tag = bs.find('p', 'booktag')
			if book_tag!=None:
				a_tags = book_tag.findAll('a')
				_bookDict['author'] = a_tags[0].get_text()
				_bookDict['category'] = a_tags[1].get_text()

				span_tags = book_tag.findAll('span')
				_bookDict['words'] = span_tags[0].get_text().replace('字数：','')
				_bookDict['readers'] = span_tags[1].get_text().replace('阅读数：','')
				_bookDict['status'] = span_tags[2].get_text()

			intro_tag = bs.find('p', id='bookIntro')
			try:
				_bookDict['cover_img'] = intro_tag.find('img').attrs['src']
			except:
				_bookDict['cover_img'] = ''
			_bookDict['summary'] = self.remove_control_chars(intro_tag.get_text())
			if _bookDict['summary'].find('<a')>=0:
				_bookDict['summary'] = ''
			# book.url = url
			# book.source = self.__class__.__name__
			# print(_bookDict)
			
			# 创建
			if book==None:
				self._writeBook([_bookDict])
				print('writed book(%d, %s)'%(book.id, book.title))
			else:
				# 更新
				(Book.update(_bookDict).where(Book.id == book.id)).execute()
				print('updated book(%d, %s)'%(book.id, book.title))

			# 短暂休息一下
			time.sleep(random.random())
		return

	# 第三步
	# 抓取目录
	# bid: 书ID
	# num: 书章节ID
	def catalog(self):
		_index = 0
		for book_source in Book_Source.select(Book_Source).join(Book, 'INNER', Book.id == Book_Source.bid).where((Book.status != '已完成') & (Book_Source.bid >= _index) & (Book_Source.source == self.__class__.__name__)):
			url = book_source.url
			bid = book_source.bid
			_chapter = Chapter.select().where((Chapter.source == self.__class__.__name__) & (Chapter.bid == bid)).order_by(Chapter.num.desc()).limit(1)
			num = 0 if len(_chapter)==0 else _chapter[0].num
			print(num)

			bs = self.get_request(url)
			
			all_list = bs.find('div', id='list-chapterAll')
			if all_list==None:
				print ({'code':'1000', 'msg':"%s:chapter need update"%(self.__class__.__name__)})
				continue

			list_tag = all_list.find('dl', 'panel-chapterlist')
			if list_tag==None:
				print ({'code':'1001', 'msg':"%s:chapter need update"%(self.__class__.__name__)})
				continue

			a_tags = list_tag.findAll('a')
			_list = []
			for k in a_tags:
				_num = int(k.attrs['href'].replace('.html', ''))
				if _num<=num:
					continue

				_chapter = Chapter.create()
				_chapter.title = k.get_text()
				_chapter.url = url + k.attrs['href']
				_chapter.num = _num
				_chapter.bid = bid
				_chapter.source = self.__class__.__name__
				_chapter.save()
				_list.append(_chapter)

				print('updated chapter(%d, %s)'%(bid, _chapter.title))
				# 短暂休息一下
				time.sleep(random.random()/10)

			_sleep = random.random()/10
			print('updated book(%d), and then sleep %s seconds.'%(bid, _sleep))
			# 短暂休息一下
			time.sleep(_sleep)
		print('done')

	## 
	# 第一步
	# 通过分类获取文章名和对应的链接
	# 
	def fiction(self):
		url = source['biquge']['category_url']
		cur_category_name = ''
		_list = {}
		for i in range(source['biquge']['category_min'], source['biquge']['category_max']):
			bs = self.get_request(url.replace('{id}', '%s'%i))

			cur_category_name = bs.find('nav', id='nav-header').find('li', 'active').get_text()
			next_page = bs.find('ul', id='pagelink')
			index_page = 1
			while next_page!=None:
				next_page = next_page.find('a', 'next')
				if next_page==None:
					break

				# 更新小说
				_page = self._cur_page(bs, cur_category_name)
				_res = self._writeBook(_page)
				print(_res, 'page index = %d, page.length = %d'%(index_page, len(_page)))
				# _list.update(_page)

				# 获取下一页数据
				bs = self.get_request(next_page.attrs['href'])
				next_page = bs.find('ul', id='pagelink')
				index_page += 1

				# 短暂休息一下
				time.sleep(random.random())

		return _list

	## 
	# 当前页面的所有小说信息
	# 
	def _cur_page(self, bs, category):
		_list = {}
		# top列表
		li_tags = bs.findAll('li', 'list-group-item')
		if li_tags==None or len(li_tags)<=0:
			return _list

		for item in li_tags:
			a_tag = item.find('a')
			_item = {'title':a_tag.get_text(), 'url': a_tag.attrs['href'], 'category': category}

			# 作者
			author = item.find('small').get_text().replace('/ ', '')
			_item['author'] = author

			# 阅读数
			readers = item.find('span').get_text()
			_item['readers'] = readers
			_item['status'] = ''

			_item['hashKey'] = self._getHashKey(_item)
			_list[_item['hashKey']] = _item

		# 最近更新列表
		tr_tags = bs.findAll('tr')
		if tr_tags==None or len(tr_tags)<=1:
			return _list

		for item in tr_tags:
			a_tag = item.find('a')
			if a_tag==None:
				continue

			_item = {'title':a_tag.get_text(), 'url': a_tag.attrs['href'], 'category': category}

			# 作者
			author = item.find('td', 'text-muted').get_text()
			_item['author'] = author

			if _item.has_key('readers') == False:
				_item['readers'] = ''

			# 状态
			status = item.findAll('td')
			_item['status'] = status[len(status)-1].get_text()

			_item['hashKey'] = self._getHashKey(_item)
			if _list.has_key(_item['hashKey'])!=True:
				_list[_item['hashKey']] = _item
			else:
				_list[_item['hashKey']]['status'] = _item['status']

		return _list

	def _getHashKey(self, book):
		return hashlib.md5(book['title'] + '_' + book['author']).hexdigest()

	def _writeBook(self, _list):
		if len(_list)==0:
			return False
		for book in _list.values():
			url = book['url']
			del book['url']
			_bid = 0
			try:
				_bid = Book.insert(book).execute()
			except:
				continue
			book_source = Book_Source.create()
			book_source.bid = _bid
			book_source.source = self.__class__.__name__
			book_source.url = url
			book_source.save()


