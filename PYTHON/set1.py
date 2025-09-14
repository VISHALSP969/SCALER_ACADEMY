s1={}       # empty dictionary
print(type(s1))

s2=set()    # empty set
print(type(s2))

s3={1,2,3,4,5,4,3,2,1}
print(s3)
print(type(s3))

#print(s3[3])   #does not support indexing

s4=set("Hello")
print(s4)
print(type(s4))

# Iteration over set
s5={10,20,30,40,50}
for i in s5:
    print(i)