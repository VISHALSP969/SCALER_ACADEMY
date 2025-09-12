a=1
b=2
c=3
d=4
print(a,b,c,d)

a,b,c,d=6,7,8,9
print(a,b,c,d)

t1=(11,22,33,44)
a,b,c,d=t1      #Unpacking of tuple
print(a,b,c,d)

t2=(11,22,33,44,55)
# a,b,c,d=t2    #Value Error - too many arguments

t3=(11,22,33)
# a,b,c,d=t3        #Value Error - not enough values

