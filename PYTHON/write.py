# new file creation
with open("text1.txt","w") as f:
    f.write("Hey new file created")

# write in an existing file
with open("text1.txt","w") as f:
    f.write("This is the updated content of our file\n")
    f.write("This is new line.")