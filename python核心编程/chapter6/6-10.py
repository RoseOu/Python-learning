#!/usr/bin/env python
# coding: utf-8

'''
字符串。写一个函数，返回一个跟输入字符串相似的字符串，要求字符串大小写反转。比如，输入“Mr.Ed”，应该返回“mR.eD”作为输出。
'''

result_list = []
def change(astring):
	for i in astring:
		if i.isupper():
			result_list.append(i.lower())
		elif i.islower():
			result_list.append(i.upper())
		else:
			result_list.append(i)
	result = ''.join(result_list)
	return result

astring = list(raw_input("Input the string here:"))
print change(astring)