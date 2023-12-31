#Program to print factorial of a given number

num = int(input("Enter the Number: "))
factorial=1
while num>0:
    factorial=factorial*num
    num=num-1

print("Factorial of a number : {}".format(factorial))
