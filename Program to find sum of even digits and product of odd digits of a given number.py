#Program to find sum of even digits and product of odd digits of a given number
Number = int(input("Enter the Number: "))
Even=0
Odd=0
while Number>0:
    digit = (Number%10)
    if digit % 2 ==0:
        Even=Even+digit
    else:
        Odd=Odd+digit
    Number=Number//10
print("Sum of the Even digits of a {} Number : {}".format(Number,Even))
print("Sum of the Odd digits of a {} Number : {}".format(Number,Odd))
