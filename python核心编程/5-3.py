# coding: utf-8


a=float(raw_input("Input your test scores:"))
if a>=90 and a<=100:
	print "Your rating score is: A"
elif a>=80 and a<=89:
	print "Your rating score is: B"
elif a>=70 and a<=79:
	print "Your rating score is: C"
elif a>=60 and a<=69:
	print "Your rating score is: D"
else:
	print "Your rating score is: F"