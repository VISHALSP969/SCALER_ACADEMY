fruits={
    "Apple":120,
    "Mango":100,
    "Pineapple":80,
    "Guava":90,
    "Orange":110
}
print(fruits)

for i in fruits:
    print(i)

for i in fruits:
    print(i,fruits[i],sep="   ")

for k,v in fruits.items():
    print(k,v,sep=" : ")