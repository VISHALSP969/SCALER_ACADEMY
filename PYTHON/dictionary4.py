fruits={
    "Apple":120,
    "Mango":100,
    "Pineapple":80,
    "Guava":90,
    "Grapes":110,
    "Orange":120
}
print(fruits)
print("Apple" in fruits)
print("Cherry" in fruits)
print("Mango" in fruits)

d=fruits.pop("Guava")
print(d)
print(fruits)

# d=fruits.pop()    # TypeError - pop expect atleast one argument

d=fruits.popitem()
print(d)
print(fruits)

del fruits
# print(fruits)     # NameError,object already deleted