#program to find sum of cubes of a number from 1 to n using while loop
n=int(input("Enter the n Value: "))
i=1
Value=0
while i<=n:
    Value = Value+(i**3)
    i=i+1

print("Sum of Cubes of 1 to {} numbers : {} ".format(n,Value))
