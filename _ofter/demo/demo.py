#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
#��ַ
url = "http://www.baidu.com/"
#����
request = urllib.request.Request(url)
#����
response = urllib.request.urlopen(request)

data = response.read()

#data = data.decode('utf-8')

print(data)

print("2")