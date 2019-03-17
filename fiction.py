#!/usr/bin/python
#coding:utf-8

import random
import requests
import re
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from config.common import source, header
import hashlib
import time
from peewee import *
from models.book_source import Book_Source
from models.book import Book
from source_factory import SourceFactory

## 
# 通过分类获取文章名和对应的链接
# 
def fiction():
	url = source['biquge']['category_url']
	cur_category_name = ''
	_list = {}
	for i in range(source['biquge']['category_min'], source['biquge']['category_max']):
		req = requests.get(url.replace('{id}', '%s'%i), headers = header[random.randint(0,4)])
		_temp_result = req.content.decode('gbk')
		bs = BeautifulSoup(_temp_result, "html.parser")

		cur_category_name = bs.find('nav', id='nav-header').find('li', 'active').get_text()
		next_page = bs.find('ul', id='pagelink')
		while next_page!=None:
			next_page = next_page.find('a', 'next')
			if next_page==None:
				break

			# 更新小说
			_page = _cur_page(bs, cur_category_name)
			_res = write(_page)
			print(_res, 'page.length = %d'%len(_page))
			# _list.update(_page)

			# 获取下一页数据
			req = requests.get(next_page.attrs['href'], headers = header[random.randint(0,4)])
			_temp_result = req.content.decode('gbk')
			bs = BeautifulSoup(_temp_result, "html.parser")
			next_page = bs.find('ul', id='pagelink')

			# 短暂休息一下
			time.sleep(random.random())

	return _list

## 
# 当前页面的所有小说信息
# 
def _cur_page(bs, category):
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

		_item['hashKey'] = getHashKey(_item)
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

		_item['hashKey'] = getHashKey(_item)
		if _list.has_key(_item['hashKey'])!=True:
			_list[_item['hashKey']] = _item
		else:
			_list[_item['hashKey']]['status'] = _item['status']

	return _list

def getHashKey(book):
	return hashlib.md5(book['title'] + '_' + book['author']).hexdigest()

def write(_list):
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
		book_source.source = 'biquge'# self.__class__.__name__
		book_source.url = url
		book_source.save()

if __name__=="__main__":
	_temp = fiction()
	print('done')