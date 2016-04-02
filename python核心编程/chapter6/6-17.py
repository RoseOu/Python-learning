#!/usr/bin/env python
# coding: utf-8

'''
方法。实现一个叫myPop()的函数。功能类似于列表的pop()方法，用一个列表作为输入，
移除列表的最新一个元素并返回它。
'''

def myPop(alist):
	alist.remove(alist[-1])
	return alist
	
alist = list(input("Input a list here:"))
print myPop(alist)