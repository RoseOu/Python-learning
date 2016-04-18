#!/usrbin/env python
#! coding: utf-8

'''
几何。创建一个由有序数值对（x，y）组成的Point类，它代表某个点的X坐标和Y坐标。
X坐标和Y坐标在实例化时被传递给构造器，如果没有给出它们的值，则默认为坐标的原点。
'''

class Point(object):
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d, %d)' % (self.x,self.y)

x = int(raw_input("Input the 'x' here:"))
y = int(raw_input("Input the 'y' here:"))
point = Point(x,y)
print point
