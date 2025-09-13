# find frequency of letters in string
text=input("Enter a string : ")
frequency={}

for i in text:
    if i not in frequency:
        frequency[i]=1
    else:
        frequency[i]+=1
print(frequency)
