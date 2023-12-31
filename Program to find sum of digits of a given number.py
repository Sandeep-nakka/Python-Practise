#Program to find sum of digits of a given number
"""
Lets take a Number : 287
Sum of digit of the number is 2+8+7=17

287%10 = 7  287//10 =28
28%10=8     28//10 =2
2%10=0

"""

Number = int(input("Enter the Number: "))
Sum=0
while Number>0:
    Sum=Sum+(Number%10)
    Number=Number//10
print("Sum of the digits of a {} Number : {}".format(Number,Sum))
