def mix(a,b,c,age=25,*args,**kwargs):
    print(a,b,c)
    print(age)
    print(args)
    print(kwargs)

# mix(1,2)      # type error - need one more positional argument
mix(1,2,3)
mix(11,22,33,30)
mix(5,10,15,27,"john","doe",hobby="reading")
