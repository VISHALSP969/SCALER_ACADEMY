def add(a,b):
    return a+b

c=add(10,5)
print(c)

r=(lambda a,b:a+b)(10,20)
print(r)

func=lambda a,b:a*b
r=func(2,7)
print(r)
print(type(func))

def larger(a,b):
    if a>b:
        return a
    else:
        return b

print(larger(2,3))

large=lambda x,y:x if x>y else y
print(large(5,7))

lst=[(12,56),(2,4),(5,3)]
lst.sort()
print(lst)

def  k(x):
    return x[1]
def  p(x):
    return x[0]+x[1]

lst.sort(key=k)
print(lst)

lst.sort(key=p)
print(lst)

lst=[(12,56),(2,4),(5,3)]
lst.sort(key=lambda x:x[1])
print(lst)
lst.sort(key=lambda x:(x[0]+x[1]))
print(lst)