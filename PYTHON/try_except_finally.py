a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
# try:
#     q=a/b
#     print("Quotient is",q)
# except:
#     print("Error!")
# print("Try again")

# try:
#     q=a/b
#     print(q)
# except Exception as e:
#     print("Error!",e)
# print("Try again")

try:
    print("Open file")
    q=a/b
except Exception as e:
    print("Error!",e)
finally:
    print("Close file")