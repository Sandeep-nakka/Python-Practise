#Program to find sum of squares of a number from 1 to n using while loop
n=int(input("Enter the n Value: "))
i=1
Value=0
while i<=n:
    Value = Value+(i*i)
    i=i+1

print("Sum of Square of 1 to {} numbers : {} ".format(n,Value))
