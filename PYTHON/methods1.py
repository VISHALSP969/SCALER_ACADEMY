class Human:
    def __init__(self,name,age,hobby):
        self.name=name
        self.age=age
        self.hobby=hobby

    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!")

obj1=Human("John",25,"Reading")
obj2=Human("Emma",23,"Cooking")
obj1.greet()
obj2.greet()
obj1.nationality="Indian"       # nationality attribute is specific to obj1
print(obj1.nationality)
# print(obj2.nationality)   # Attribute Error
obj2.hobby="Social Service"     # changing attribute of particular object
print(obj2.hobby)
