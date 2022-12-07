def f1(n):
    return lambda x:x*n
d=f1(1) #value is assigned to n
print(d(15)) #value will be assigned to x
d1=f1(2)
print(d1(15))

