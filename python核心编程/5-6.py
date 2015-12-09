# coding: utf-8

t=1
while(t):
	a=raw_input("Input a impression here:")
	if '+' in a:
		x,y=a.split('+',1)
		print float(x)+float(y)
		t=0
	elif '-' in a:
		x,y=a.split('-',1)
		print float(x)-float(y)
		t=0
	elif '**' in a:
		x,y=a.split('**',1)
		print float(x)**float(y)
		t=0
	elif '/' in a:
		x,y=a.split('/',1)
		print float(x)/float(y)
		t=0
	elif '%' in a:
		x,y=a.split('%',1)
		print float(x)%float(y)
		t=0
	elif '*' in a:
		x,y=a.split('*',1)
		print float(x)*float(y)
		t=0
	else:
		print "Wrong expression,input again."