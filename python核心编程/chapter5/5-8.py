# coding: utf-8

#题目：几何。计算面积和体积(a)正方形和立方体(b)圆和球


from math import pi
type=raw_input('选择你要计算的:A.正方形的面积,B.立方体的体积,C.圆的面积,D.球的体积'.decode('utf-8').encode('gbk'))

#计算正方形的面积
if type=='A':
	a=float(raw_input('输入正方形的边长:'.decode('utf-8').encode('gbk')))
	s=a**2
	print s

#计算立方体的体积
elif type=='B':
	b=float(raw_input('输入立方体的棱长:'.decode('utf-8').encode('gbk')))
	v=b**3
	print v

#计算圆的面积
elif type=='C':
	r=float(raw_input('输入圆的半径:'.decode('utf-8').encode('gbk')))
	s1=pi*r**2
	print s1

#计算球的体积
else:
	r1=float(raw_input('输入球的半径:'.decode('utf-8').encode('gbk')))
	v1=4*pi*r1**3/3
	print v1