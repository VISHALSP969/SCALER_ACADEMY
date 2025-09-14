# Updating a set
s={1,2,3,4,5,4,5}
print(s)

s.add(8)
print(s)
s.add(7)
print(s)
s.add(8)
print(s)

text="Hello"
s.update(text)
print(s)

#Delete an item
s={'w','e','l','c','o','m','e'}
print(s)
i=s.pop()
print(i)
print(s)
i=s.pop()
print(i)
print(s)

s={1,2,3,2,1}
print(s)
i=s.remove(2)
print(i)
print(s)
s=set("hello")
print(s)
s.remove("h")
print(s)
s.remove("o")
print(s)