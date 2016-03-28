#!/usr/bin/env python
# coding: utf-8

'''
约数。完成一个名为getfactors()的函数。它接受一个整型作为参数，返回它所有约数的列表，包括1和它本身。
'''

num = int(input("Input the number here:"))
def getfactors(num):
	fac_list = []
	i = 1
	while i <= num:
		if num%i == 0:
			fac_list.append(i)
		i = i+1
	return fac_list
print getfactors(num)
