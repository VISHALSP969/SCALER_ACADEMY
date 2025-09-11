l=list()    # empty list
print(type(l))
print(l)

l1=[1,2,3,4,5]
print(type(l1))
print(l1)
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[-1])
print(l1[-2])
print(l1[-3])
print(l1[-4])
print(l1[-5])
print(f"Length={len(l1)}")
l1[2]=7
print(l1)
print(f"Id={id(l1)}")
l1[3]=8
print(l1)
print(f"Id={id(l1)}")

l2=[1]
print(type(l2))
print(l2)

l3=list((1,2,3))
print(type(l3))
print(l3)

for i in l1:
    print(i)