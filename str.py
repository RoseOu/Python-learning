# -*- coding: UTF-8 -*-           

#Multiline input
stop=''
input=''
for str in iter(raw_input,stop):
	input+=str+'\n'

#change capital into lowercase and serparate the string
input1=input.lower().split('\n')	   


#start
import time
t1=time.time()

#transformation
for str in input1:
	n=0
	for i in str:
		if ord(i) in range(97,123):
			n=n+ord(i)-96
		else:
			pass
	print n
	
#end
t2=time.time()

#running time
print (t2-t1)*1000,'ms'	
