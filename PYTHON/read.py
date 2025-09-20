with open("text2.txt","r") as f:
    # content=f.read()    # read all  the content
    content=f.read(10)  # reads only the specified length of characters
    print(content)
    # content=f.read(6)     # reads the 6 characters after first 10 characters
    # print(content)

    # tells the position of file handle
    print(f.tell())

    # resetting the file handler
    f.seek(2)
    print(f.tell())
    content=f.read()
    print(content)

    f.seek(0)
    print(f.tell())
    content=f.readline()    # read a single line
    print(content)
    content=f.readline()
    print(content)

    f.seek(0)
    content=f.readlines()   # read all lines, returned data is list
    print(content)
