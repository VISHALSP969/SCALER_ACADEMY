name="john doe"
print(name.capitalize())
print(name.title())
name="JOHN DOE"
print(name.lower())
name="john doe"
print(name.upper())
print(name.find("doe"))
print(name.find("john"))
print(name.count("doe"))
print(name.count("o"))
print(name.count("z"))
print(name.index("j"))
print(name.index("o"))
print(name.rindex("o"))
print(name.index("john"))
name="john doe doe"
print(name.index("doe"))
print(name.rindex("doe"))
name="john doe"
print(name.replace("doe","kennedy"))
print(name.split(" "))
name="john doe doe doe"
print(name.split(" "))
print(name.split(" ",1))
print(name.split(" ",2))

name="john doe"
print(name.isupper())
print(name.islower())
name="JOHN DOE"
print(name.isupper())
print(name.islower())
name="John Doe"
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.isalnum())
name="12345"
print(name.isnumeric())
name="john123"
print(name.isalpha())
print(name.isalnum())
print(name.isnumeric())
name="john doe"
print(name.isascii())
