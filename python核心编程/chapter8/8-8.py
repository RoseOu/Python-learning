#!/usr/bin/env python
#! coding: utf-8

'''
阶乘。一个数的阶乘被定义为从1到该数字所有数字的乘积。N的阶乘简写为N！。
N！== factorial(N) == 1*2*3*...*(N-2)*(N-1)*N。如4! == 1*2*3*4。写一个函数，
指定N，返回N！的值。
'''

def myfactorial(num):
	i = 1
	result = 1
	while i <= num:
		result = result*i
		i = i + 1
	return result

num = int(input("Input the number here:"))
print myfactorial(num)