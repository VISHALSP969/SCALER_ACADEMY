def test(*args):
    print(args)
    for i in args:
        print(i*i,end="  ")
    print()

test(2)
test(2,4)
test(2,4,6)