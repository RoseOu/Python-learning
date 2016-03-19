#! /usr/bin/env python
# coding: utf-8
 
'''
6–8.
列表.给出一个整数值,返回代表该值的英文,比如输入 89 返回"eight-nine"。
附加题:
能够返回符合英文语法规则的形式,比如输入“89”返回“eighty-nine”。本练习中的值限定在家 0
到 1,000.
'''

#(1)
def f(num):
	num_list = list(str(num))
	eng = "zero,one,two,three,four,five,six,seven,eight,nine,ten"
	eng_list = eng.split(',')
	result = []
	for i in num_list:
		result.append(eng_list[int(i)])
	return '-'.join(result)
num = int(raw_input("Input the number here:"))
print f(num)


#附加题
#附加题
def g(num):
	num_list = list(str(num))
	eng = "zero,one,two,three,four,five,six,seven,eight,nine,ten"
	eng_list = eng.split(',')
	result = []
	for i in num_list；
		if num <= 10:
			result.append（eng_list[int(i)])
		return result
		elif 