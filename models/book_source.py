#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from peewee import *
from entry import Entry

class Book_Source(Entry):
	##
	# bid：book表ID
	# source：来源
	# disable：状态标记
	# 
	bid = IntegerField()
	source = CharField()
	url = CharField()
	disable = CharField()