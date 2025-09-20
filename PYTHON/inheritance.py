# parent class
class Human:
    population = 0
    names = []

    def __init__(self, name, age,alive=True):
        self.name = name
        self.age = age
        self.alive=alive
        Human.population += 1
        Human.names.append(name)

    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!")

    def dead(self):
        if self.alive:
            Human.population-=1
            Human.names.remove(self.name)
            self.alive=False
            print(f"{self.name} is no more now")
        else:
            print("This person already dead!")

    def children(self,number,*args):
        Human.population+=1
        for name in args:
            Human.names.append(name)

obj1=Human("John",25)
print(Human.population)
print(Human.names)
obj2=Human("Emma",23)
print(Human.population)
print(Human.names)
obj1.greet()
obj2.greet()
obj1.nationality="Indian"       # nationality attribute is specific to obj1
print(obj1.nationality)
# print(obj2.nationality)   # Attribute Error
obj2.age=22     # changing attribute of particular object
print(obj2.age)

obj3=Human("Jacob",75,"Reading")
print(Human.population)
print(Human.names)
obj4=Human("Mary",65,"Gardening")
print(Human.population)
print(Human.names)

obj3.dead()
print(Human.population)
print(Human.names)
obj3.dead()
print(Human.population)
print(Human.names)
obj1.children(1,"Laila")
print(Human.population)

# derived class
class Employee(Human):
    def __init__(self,name,age,company,position):
        super().__init__(name,age)
        self.company=company
        self.position=position

    def hire(self,person):
        print(f"{person} has been hired in our company")
        Human.names.append(person)
        Human.population+=1

e1=Employee("Bravo",21,"Amazon","SDE")
print(Human.population)
print(Human.names)
e1.greet()
print(e1.name)
e2=Employee("Simon",23,"Intel","Business Analyst")
print(Human.population)
print(Human.names)
e2.greet()
print(e2.name)

e1.hire("Albert")
print(Human.names)
print(Human.population)
