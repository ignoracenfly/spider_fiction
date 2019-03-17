#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from peewee import *
from config.db import *

db = MySQLDatabase(db['database'], user=db['user'], password=db['password'], host=db['host'], port=db['port'], charset = db['charset'])

class Entry(Model):
	class Meta:
		database = db