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
from config import source
from config import header

##
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
def summary(url):
	_result={'title':'', 'author':'', 'category':'', 'words':'', 'readers':'', 'status':'', 'cover_img':'', 'summary':''}

	req = requests.get(url,headers = header[random.randint(0,4)])
	_temp_result = req.content.decode('gbk')
	bs = BeautifulSoup(_temp_result, "html.parser")
	
	title_tag = bs.find('h1', 'bookTitle')
	if title_tag!=None:
		_result['title'] = title_tag.get_text()

	book_tag = bs.find('p', 'booktag')
	if book_tag!=None:
		a_tags = book_tag.findAll('a')
		_result['author'] = a_tags[0].get_text()
		_result['category'] = a_tags[1].get_text()

		span_tags = book_tag.findAll('span')
		_result['words'] = span_tags[0].get_text()
		_result['readers'] = span_tags[1].get_text()
		_result['status'] = span_tags[2].get_text()

	intro_tag = bs.find('p', id='bookIntro')
	_result['cover_img'] = intro_tag.find('img').attrs['src']
	_result['summary'] = intro_tag.get_text().replace('\n\r\n                            ','').replace('\r\n                        ','')

	return _result


if __name__=="__main__": 
    _temp = summary('http://www.biqukan.cc/book/47583/')
    print(_temp)