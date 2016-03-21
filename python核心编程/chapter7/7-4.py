#!/usr/bin/env python
# coding: utf-8

'''
7-4. 建立字典。给定两个长度相同的列表，比如说，列表[1,2,3,...]和['abc','def','ghi',...],用这两个列表里的所有数据组成一个字典,像这样：{1:'abc', 2: 'def', 3: 'ghi',...}
'''

key = raw_input("Input here:")
keylist = list(key.split(','))
value = raw_input("Input here:")
valuelist = list(value.split(','))
thedict = dict(zip(keylist,valuelist))
print thedict