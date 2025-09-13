fruits={
    "Apple":120,
    "Mango":100,
    "Pineapple":90,
    "Banana":70
}
print(fruits)

print(fruits["Apple"])
print(fruits["Mango"])
print(fruits["Pineapple"])
print(fruits["Banana"])

# print(fruits["Guava"])    # Key Error

print(fruits.get("Apple"))
print(fruits.get("Mango"))
print(fruits.get("Pineapple"))
print(fruits.get("Banana"))

print(fruits.get("Guava"))      # not shows key error, returns None
print(fruits.get("Guava","Item not found"))