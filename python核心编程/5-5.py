# coding: utf-8
t=1
while(t):
	a=float(raw_input("Input a number from 0 to 1:"))
	if a>0 and a<1 or a==0 or a==1:
		a=a*100
		a25=a/25
		a10=(a%25)/10
		a5=(a%25%10)/5
		a1=a%25%10%5
		print "You can change %d quarter dollars,%d dimes,%d nickels,%d cents." % (a25, a10, a5, a1)
		t=0
	else:
		print "Wrong,please input again."