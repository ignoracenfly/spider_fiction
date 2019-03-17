#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from factory.biquge import biquge

##
# 抓取小说正文
#
class SourceFactory:
	def __init__(self, source, url):
		self.source = source
		self.url = url
		self.globals = globals()


	def get(self):
		return self.globals.get(self.source)(self.url)