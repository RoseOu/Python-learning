#!/usr/bin/env python
# coding: utf-8

'''
素数。我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素数。
把相关代码转换为一个返回值为布尔值的函数，函数名为isprime()。如果输入的是一个素数，
那么返回True，否则返回False。
'''

num = int(input("Input the number here:"))
divisor = []
primelist = [1,num]
def isprime(num):
	i = 1
	while i <= num:
		if num % i == 0:
			divisor.append(i)
		else:
			pass
		i = i + 1
	if divisor == primelist:
		return True
	elif num == 1:
		return True
	else:
		return False

print isprime(num)