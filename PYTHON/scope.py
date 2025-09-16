a=5     # global variable
def func():
    print(a)
func()
print(a)

def func1():
    a=10    # local variable
    print(a)
func1()
print(a)

def func2():
    a=5
    print(a)
func2()
print(a)

x=10
print(x)
def func3():
    global x
    x=20
func3()
print(x)
