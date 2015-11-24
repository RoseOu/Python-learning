# -*- coding: UTF-8 -*-

#Enter the word and change capital into lowercase
a=raw_input("Enter the word here:").lower().split(' ')

#Function
def f(x):
	if x[0] in 'aeiou':
		x+='hay'
		print x,
	else:
		pass

def g(x):
    if x[:2]=='qu':
        x=x[2:]+'quay'
        print x,
    else:
        pass
		
def h(x):
	def y(x):
		if x[0] in 'aeiou':
			return False
		else:
			for y in range(1,len(x)):
				if x[y] in 'aeiouy':
					return y
					break
	i=y(x)
	if y(x)==False:
		pass
	else:
		x=x[i:]+x[:i]+'ay'
		print x,


for x in a:
		f(x)
		g(x)
		h(x)