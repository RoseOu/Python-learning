#!/usr/bin/env python
# coding: utf-8

'''
素因子分解。以8-4和8-5练习中的isprime()和getfactors()函数为基础编写一个函数，
它接受一个整型作为参数，返回该整形所有素数因子列表。这个过程叫求素因子分解，
它输出的所有因子之积应该是原来的数字。注意列表里可能有重复的元素。例如输入20，
返回结果应该是[2,2,5].
8-4题目：素数。本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素数。
把相关代码转换为一个返回值为布尔值的函数，函数名为isprime()。如果输入的是一个素数，
那么返回True，否则返回False。
8-5题目：约数。完成一个名为getfactors()的函数。它接受一个整型作为参数，
返回它所有约数的列表，包括1和它本身。
'''

def isprime(num):
	divisor = []
	primelist = [1,num]
	i = 1
	while i <= num:
		if num % i == 0:
			divisor.append(i)
		else:
			pass
		i = i + 1
	if divisor == primelist:
		return True
	else:
		return False

def getfactors(num):
	fac_list = []
	i = 1
	while i <= num:
		if num%i == 0:
			fac_list.append(i)
		i = i+1
	return fac_list

def prime_factor(num):
	primefactor = []
	factor = getfactors(num)
	numb = 1
	for i in factor:
		if isprime(i):
			primefactor.append(i)
		else:
			pass
	for m in primefactor:
		numb = numb*m
	if numb == num:
		return primefactor
	else:
		primefactor.append(num/numb)
		primefactor.sort()
		return primefactor


num = int(input("Input the number here:"))
print prime_factor(num)