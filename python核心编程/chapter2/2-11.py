# coding: utf-8

#the funtion of get the total of five numbers
def Total():
	a=[1,2,3,4,5]
	i=0
	total=0
	for i in range(0,5):
		print 'Input number', i+1
		a[i]=float(raw_input())
		total=total+a[i]
	print 'Total:',total

#the funtion of get the average of five numbers
def Average():
	a=[1,2,3,4,5]
	i=0
	total=0
	for i in range(len(a)):
		print 'Input number', i+1
		a[i]=float(raw_input())
		total=total+a[i]
	print 'average:',total/5

#User's choice	
print 'Please choose what you want to do:'
print '(1)If you want to get the total of five numbers,please input "a".'
print '(2)If you want to get the average of five numbers,please input "b".'
print '(3)If you want to quit,please input "X." \n'
choice = raw_input('Your choice:')

#Program
if choice=='a':
	Total()
if choice=='b':
	Average()
if choice=='X':pass
