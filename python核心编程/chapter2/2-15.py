# coding: utf-8


#把数字从小到大排列
print 'Input your numbers here:'
number1=raw_input()
number2=raw_input()
number3=raw_input()

if number1>number2>number3:
	print number3,number2,number1
elif number1>number3>number2:
	print number2,number3,number1
elif number2>number1>number3:
	print number3,number1,number2
elif number2>number3>number1:
	print number1,number3,number2
elif number3>number1>number2:
	print number2,number1,number3
else:
	if number3>number2>number1:
		print number1,number2,number3


#把数字从大到小排列
print 'Input your numbers here:'
number1=raw_input()
number2=raw_input()
number3=raw_input()

if number1>number2>number3:
	print number1,number2,number3
elif number1>number3>number2:
	print number1,number3,number2
elif number2>number1>number3:
	print number2,number1,number3
elif number2>number3>number1:
	print number2,number3,number1
elif number3>number1>number2:
	print number3,number1,number2
else:
	if number3>number2>number1:
		print number3,number2,number1