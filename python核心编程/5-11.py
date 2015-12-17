# coding: utf-8

"""
题目：取余。
(a) 使用循环和算术运算，求出 0－20 之间的所有偶数
(b)同上,不过这次输出所有的奇数
(c)综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么？
(d)使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 先要求用户输入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回 True 和 False;
"""

type=raw_input('Choose:a.求出0－20之间的所有偶数,b.求出0－20之间的所有奇数，c.检测一个整数能否被另一个整数整除'.decode('utf-8').encode('gbk'))

if type=='a':
	for i in range(1,21):
		if i%2==0:
			print i
		else:
			pass
		
elif type=='b':
	for i in range(1,21):
		if i%2==1:
			print i
		else:
			pass

else:
	x=float(raw_input('Input the first number:'))
	y=float(raw_input('Input the second number:'))
	if x%y==0 or y%x==0:
		print 'True'
	else:
		print 'False'
	
