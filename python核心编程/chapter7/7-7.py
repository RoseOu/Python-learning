#!/usr/bin/env python
# coding: utf-8

'''
颠倒字典中的键和值。用一个字典做输入，输出另一个字典，用前者的键做值，前者的值做键。
'''

adict = input("Input a dictionary here:")

def changedict(adict):
	keylist = adict.keys()
	valuelist = adict.values()
	result = zip(valuelist,keylist)
	return dict(result)

if type(adict) != dict:
	print "Invalid input!please input again."
else:
	print changedict(adict)