with open("bin.jpg","rb") as f:
    data=f.read()
    print(data)

    with open("new.jpeg","wb") as f1:
        f1.write(data)