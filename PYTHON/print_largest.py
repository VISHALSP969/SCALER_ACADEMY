marks=[90,30,100,50.80,95]
highest=marks[0]
for i in marks:
    if i>highest:
        highest=i
print(f"Highest = {highest}")
print(max(marks))

lowest=marks[0]
for i in marks:
    if i<lowest:
        lowest=i
print(f"Lowest = {lowest}")
print(min(marks))