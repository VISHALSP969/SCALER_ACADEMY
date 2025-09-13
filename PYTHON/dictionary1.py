d1={}   #empty dictionary
print(d1)
print(type(d1))

d2=dict()   #empty dictionary
print(d2)
print(type(d2))

fruits1={
    "Apple":120,
    "Mango":100,
    "Pineapple":90
}
print(fruits1)
print(type(fruits1))

name=["Apple","Mango","Pineapple"]
price=[120,100,90]
# print(zip(name,price))    # zip object
fruits2=dict(zip(name,price))
print(fruits2)
print(type(fruits2))

print(len(fruits2))