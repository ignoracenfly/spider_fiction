#!/usr/bin/python
#coding:utf-8

import time
from peewee import *
from models.book_source import Book_Source
from models.chapter import Chapter
from source_factory import SourceFactory


if __name__=="__main__":
	bid = 1
	book = Book_Source.select().where(Book_Source.id == bid)
	_list = Chapter.select(Chapter.source, fn.max(Chapter.num).alias('num')).where(Chapter.bid == bid).group_by(Chapter.source)

	if len(_list)==0:
		_list = []
		for item in book:
			_chapter = Chapter()
			_chapter.source = item.source
			_chapter.num = 0
			_chapter.url = item.url
			_list.append(_chapter)
	else:
		for item in book:
			for _item in _list:
				if item.source == _item.source:
					_item.url = item.url
					break


	# 获取各来源的最新章节
	for item in _list:
		factory = SourceFactory(item.source, item.url)
		_res = factory.get().catalog(bid, item.num)
		# print(_res)
		print("%s, %s, %d done."%(_res['code'], _res['msg'], len(_res['data'])))
		time.sleep(1)

