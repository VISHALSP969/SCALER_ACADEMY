def func():
    return 1,2,3

a,b,c=func()
print(a,b,c)
print(type(a),type(b),type(c))

r=func()
print(r)
print(type(r))

def func1(name,age):
    return name,age

r=func1("John",25)
print(r)
print(type(r))
n,a=func1("Michael",27)
print(n,a)
print(type(n),type(a))