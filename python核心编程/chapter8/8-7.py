#!/usr/bin/env python
# coding: utf-8

'''
完全数。完全数被定义为这样的数字：它的约数（不包括它自己）之和为它本身。
例如：6的约数是1,2,3，因为1+2+3=6，所以6被认为是一个完全数。编写一个名为isperfect()的函数，
它接受一个整形作为参数，如果这个数字是完全数，返回1，否则返回0.
'''

num = int(input("Input the number here:"))
def isperfect():
	m = 0
	i = 1
	while i < num:
		if num%i == 0:
			m = m + i
		i = i + 1
	if num == m:
		return 1
	else:
		return 0
print isperfect()
