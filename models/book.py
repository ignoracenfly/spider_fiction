#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from peewee import *
from entry import Entry
import hashlib

class Book(Entry):
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
	# hashKey：title + author hash
	title = CharField()
	author = CharField()
	category = CharField()
	words = CharField()
	readers = CharField()
	status = CharField()
	cover_img = CharField()
	summary = CharField()
	source = CharField()
	hashKey = CharField()
	url = CharField()

	def setHash(self):
		self.hashKey = hashlib.md5(self.title + '_' + self.author).hexdigest()