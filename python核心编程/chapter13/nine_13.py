
#!/usr/bin/env python
# coding: utf-8

'''
13-9.队列类。一个队列（queue）是一种具有先进先出（first-in-first-out，FIFO）特性的数据结构。一个队列就像是一行队伍，数据从前端被移除，从后端被加入。
这个类必须支持下面几种方法： enqueue()在列表的尾部加入一个新的元素。dequeue()在列表的头部取出一个元素，返回它并且把它从列表中删除。
'''

class queue(list):
	def enqueue(self,x):
		self.append(x)
	def dequeue(self,):
		ele = self[0]
		self.pop(0)
		return ele




