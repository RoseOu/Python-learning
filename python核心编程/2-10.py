# coding: utf-8


t=1
while (t):
	a=(float(raw_input('Input a number between 1 and 100:')))
	if a>1 and a<100 or a==1 or a==100:
		print 'Right',a
		t=0
	else:
		print 'You print a false number,please try again.'