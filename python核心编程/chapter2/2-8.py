# coding: utf-8

#while
a=[1,2,3,4,5]
i=0
total=0
while (i<5):
    print 'Input number', i+1
    a[i]=float(raw_input())
    total=total+a[i]
    i=i+1
print 'Total:', total

#for
a=[1,2,3,4,5]
i=0
total=0
for i in range(0,5):
    print 'Input number', i+1
    a[i]=float(raw_input())
    total=total+a[i]
print 'Total:',total