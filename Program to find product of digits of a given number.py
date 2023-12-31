#Program to find product of digits of a given number
Number = int(input("Enter the Number: "))
product=1
while Number>0:
    product=product*(Number%10)
    Number=Number//10
print("Product of the digits of a {} Number : {}".format(Number,product))
