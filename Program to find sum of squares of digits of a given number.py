#Program to find sum of squares of digits of a given number
Number = int(input("Enter the Number: "))
Sum=0
while Number>0:
    Sum=Sum+((Number%10)**2)
    Number=Number//10
print("Sum of the digits of a {} Number : {}".format(Number,Sum))
