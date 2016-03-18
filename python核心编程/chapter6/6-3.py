#!/usr/bin/env python
# coding: utf-8

'''
6–3. 排序
(a) 输入一串数字,从大到小排列之.  
(b) 跟a 一样,不过要用字典序从大到小排列之.  
'''

#（a）
list1 = input("Input the numbers:")
alist = sorted(list1)
alist = list(alist)
alist.reverse()
print alist

#(b)
blist = []
list2 = input("Inter the numbers:")
for i in list2:
	eachnum = str(i)
	blist.append(eachnum)
blist = sorted(blist)
blist.reverse()
print blist

