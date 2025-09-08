i=1
sum=0
sum_even=0
while i<=10:
    if i%2==0:
        sum_even+=i
    sum+=i
    i+=1
print(f"Sum = {sum}")
print(f"Sum of even numbers = {sum_even}")