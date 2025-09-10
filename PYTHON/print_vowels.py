# Print all vowels of a given string
text="The quick brown fox jumps over the lazy dog"
for i in text:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print(i,end=" ")
print()

for i in text:
    if i in "aeiou":
        print(i,end=" ")
print()