fruits={
    "Apple":120,
    "Mango":100,
    "Pineapple":90
}
print(fruits)
fruits["Pineapple"]={"small":90,"large":120}
print(fruits)
fruits["Cherry"]=130
print(fruits)

f1={"Grapes":110,"Orange":120}
fruits.update(f1)
print(fruits)