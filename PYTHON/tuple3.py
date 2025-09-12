t1=(2,3,4)
# t1[0]=1    #TypeError,does not support item assignment

t2=([2,3,4,5],"Welcome")
print(type(t2))
print(id(t2))
print(t2[0])
print(type(t2[0]))
print(t2[1])
print(type(t2[1]))
t2[0][0]=1
print(t2)
print(id(t2))