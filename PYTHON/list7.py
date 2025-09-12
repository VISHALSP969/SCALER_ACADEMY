for i in range(10):
    print(i)

l=[]
for i in range(10):
    l.append(i)
print(l)

# list comprehension
l1=[i for i in range(10)]
print(l1)

l2=[i*i for i in range(10)]
print(l2)

l3=[i**3 for i in range(10) if i%2==0]
print(l3)