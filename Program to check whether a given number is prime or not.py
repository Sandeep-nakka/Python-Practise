#Program to check whether a given number is prime or not
num = int(input("Enter the Number: "))
i=1
count=0
while i<=num:
    if num % i == 0:
        count=count+1
    i=i+1

if count == 2:
    print("{} is a Prime Number".format(num))
else:
    print("{} is not a Prime Number".format(num))
