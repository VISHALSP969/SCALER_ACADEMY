class Human:
    population=0
    names=[]
    def __init__(self,name,age,hobby):
        self.name=name
        self.age=age
        self.hobby=hobby
        Human.population+=1
        Human.names.append(name)

    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!")

obj1=Human("John",25,"Reading")
print(Human.population)
print(Human.names)
obj2=Human("Emma",23,"Cooking")
print(Human.population)
print(Human.names)
