#!/usr/bin/env python
# coding: utf-8

'''
循环。编写一个程序，让用户输入三个数字：(f)rom,(t)o,(i)ncrement。以i为步长，
从f计数到t，包括f和t。例如，如果输入的是f==2,,t==26，i==4，程序将输出2,6，
10,14,18,22,26.
'''

f = int(input("Input the 'from' here:"))
t = int(input("Input the 'to' here:"))
i = int(input("Input the 'increment' here:"))
x = f
while x <= t:
	print x,
	x = x + i