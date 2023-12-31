#Program to find the sum of the numbers from 1 to n using while loop
n=int(input("Enter the n Value: "))
i=1
Value=0
while i<=n:
    Value = Value+(i)
    i=i+1

print("Sum of 1 to {} numbers : {} ".format(n,Value))
