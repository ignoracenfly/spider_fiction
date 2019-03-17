#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
from config_old import header
import random
import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

class SourceTemplate:
	def __init__(self, url):
		self.url = url

	# 拼音还原
	py_dict = {'jīngshén':'精神', '。。。。。。':'……', '。。。':'…', '帝**神': '帝国军神'}
	# 垃圾过滤
	dirt_dict = ['皐ww\.。　', 'br/\>', '--\>\>', '一秒记住.*免费读！', '    \*', '\(未完待续.*\)T']

	def filter(self, content):
		content = content.encode('utf8')
		# 一次过滤
		for v in self.dirt_dict:
			content = re.sub(v, "", content)

		for key in self.py_dict:
			content = content.replace(key, self.py_dict[key])

		content = content.decode('utf8')
		_temp = content.split('\r\n')

		# 二次次过滤
		for index in range(len(_temp)):
			_temp[index] = _temp[index].strip(' ').strip('\r').strip('\n')

		# 三次过滤
		_temp = [elem for elem in _temp if elem != None and len(elem) > 1]

		# 翻页拼接
		for index in range(len(_temp)):
			if _temp[index].find(' ')<0 and index>0 and len(_temp[index])>1:
				_temp[index-1] += _temp[index]
				_temp[index] = ''

		# 四次过滤
		_temp = [elem for elem in _temp if elem != None and len(elem) > 1]
		return '<br>'.join(_temp)

	def remove_control_chars(self, s):
		control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
		control_char_re = re.compile('[%s]' % re.escape(control_chars))
		return control_char_re.sub('', s).strip()

	def get_request(self, url):
		req = requests.Session()
		req.mount('http://', HTTPAdapter(max_retries = 3))
		req.mount('https://', HTTPAdapter(max_retries = 3))
		
		req = req.get(url, headers = header[random.randint(0,4)], timeout = (3, 10))
		try:
			_temp = req.content.decode('gbk', errors='replace')
			return BeautifulSoup(_temp, "html.parser")
		except requests.exceptions.RequestException as e:
			print(e)
		except UnicodeDecodeError as e:
			print(e)





