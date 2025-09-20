lst=[1,2,3]
print(len(lst))
str1="Hello"
print(len(str1))
tup1=(5,6,7,8)
print(len(tup1))

def mul(*args):
    total=1
    for i in args:
        total*=i
    return total

print(mul(1))
print(mul(1,2))
print(mul(1,2,3))
print(mul(1,2,3,4))

class Human:
    def speak(self,language):
        print("I speak",language)

h1=Human()
h2=Human()

h1.speak("Hindi")
h2.speak("English")
h1.speak("German")
