f=open("name.txt") # by default in read mode
print(f)
print(type(f))
print(f.closed)     # check file closed or not
str1=f.read()   # read all content
print(str1)
# str1=f.read(10)   # reads only 1 characters
# print(str1)
f.close()
print(f.closed)

# write operation
f=open("sample.txt","w")
f.write("I'm writable")
f.close()