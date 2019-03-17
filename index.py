#!/usr/bin/python
#coding:utf-8

# 小说列表
# fictions
#
# 小说介绍信息
# summary
#
# 某本小说的目录列表
# bid 小说ID
# chapters
# 
# 某一章节的详细内容
# url 当前章节的URL
# article
# 
# print("content-type:text/html")
# print("<html>任何想要显示的内容</html>")

def ajax(code, msg, data):
	# print("content-type:text/html")
	print('content-type:application/json')
	print("")

	# print('<meta charset="UTF-8">')
	# print(data)
	_res = {'code': code, 'msg':msg, 'data': data}
	print(json.dumps(_res))

def debug_log(data):
	print("content-type:text/html")
	print("")
	print('<meta charset="UTF-8">')
	print(data)


from source_factory import SourceFactory
import json
factory = SourceFactory('biquge', 'http://www.biqukan.cc/book/20216/16716957.html')
# debug_log('')
_temp = factory.get().article()
# print(_temp['content'])
ajax(0, '', _temp)

