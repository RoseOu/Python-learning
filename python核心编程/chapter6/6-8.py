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
num_list = int(raw_input("Input the number here:"))
eng = "zero,one,two,three,four,five,six,seven,eight,nine"
eng_list = list(eng.split(','))
get_list = list(str(num_list))
result = []
for i in get_list:
    result.append(eng_list[int(i)])
 
print '-'.join(result)

#附加题