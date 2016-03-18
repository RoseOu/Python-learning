#!/usr/bin/env python
# coding: utf-8

'''
题目：创建一个 string.strip()的替代函数:接受一个字符串,去掉它前面和后面的空格
'''
def StringStrip(astring):
	while astring[0] == ' ':
		astring = astring[1:]
	while astring[-1] == ' ':
		astring = astring[:-1]
	return astring

astring = raw_input("Input a string here:")
print StringStrip(astring)