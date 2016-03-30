#!/usr/bin/env python
# coding:utf-8

'''
斐波那契数列。斐波那契数列形如1,1,2,3,5,8,13,21，等等。也就是说，下一个值是序列中前两个值之和。
写一个函数，给定N，返回第N个斐波那契数字。例如，第1个斐波那契数字是1，第6个是8.
'''

def fibonacci(n):
	i = 3
	firstlist = [1,1]
	if n == 1 or n ==2:
		return 1
	else:
		result = sum(firstlist)
		while n > i:
			firstlist.pop(0)
			firstlist.append(result)
			result = sum(firstlist)
			i = i + 1
		return result

n = int(input("Input the number here:"))
print fibonacci(n)