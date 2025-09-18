def intro(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,":",value)

intro(name="John")
intro(name="Michael",age=25)
intro(name="Thomas",age=27,hobby="Reading")
