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
<<<<<<< HEAD
for i in range(0,5):
    print 'Input number', i+1
    a[i]=float(raw_input())
    total=total+a[i]
print 'Total:',total
=======
a=[1,2,3,4,5]
i=0
for i in range(0,5):
    print 'Input number',i+1
    a[i]=float(raw_input())
    total=total + a[i]
print 'Total:',total
>>>>>>> 087293379bbe8dae51ba74bf5fbc1be0a5350e37
