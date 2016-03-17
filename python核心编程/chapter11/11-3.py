#!/usr/bin/env python
# coding: utf-8

'''
在这个练习中，我们将实现max()和min()内建函数。
(a) 写分别带两个元素返回一个较大和较小元素，简单的max2()和min2()函数。他们应该可以用任意的python对象运作。举例来说，max2(4,8)和min2(4,8)会各自每次返回8 和4。
(b)创建使用了在a部分中的解来重构max()和min()的新函数my_max()和my_min().这些函数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。用数字和字符串来测试你的解。
'''

#(a)
def max2(x,y):
	if x > y:
		return x
	else:
		return y

def min2(x,y):
	if x < y:
		return x
	else:
		return y

#(b)
def my_max(*nums):
	maxnum = nums[0]
	for eachnum in nums:
		maxnum = max2(maxnum,eachnum)
	return maxnum

def my_min(*nums):
	minnum = nums[0]
	for eachnum in nums:
		minnum = min2(minnum,eachnum)
	return minnum

x = float(raw_input("Input the first number:"))
y = float(raw_input("Input the second number:"))
print "The max:",max2(x,y)
print "The min:",min2(x,y)
nums = input("Input the numbers and use ',' to divide them:")
print "The max:",my_max(*nums)
print "The min:",my_min(*nums)