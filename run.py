#!/usr/bin/python
#coding:utf-8

from source_factory import SourceFactory

if __name__=="__main__":
	factory = SourceFactory('biquge', '')
	# _temp = factory.get().article()
	# _temp = factory.get().summary()

	# step 1
	# _temp = factory.get().fiction()

	# step 2
	# _temp = factory.get().summary()

	# step 3
	_temp = factory.get().catalog()
	print(_temp)