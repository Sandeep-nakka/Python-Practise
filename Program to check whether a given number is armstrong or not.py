#Program to check whether a given number is armstrong or not

# 153 = 1*1*1 + 5*5*5 + 3*3*3

Number = int(input("Enter the Number: "))
Sum=0
temp=Number

while temp>0:
    Sum=Sum+(temp%10)**3
    temp=temp//10

if Sum == Number:
    print("{} is a Amstrong Number".format(Number))
else:
    print("{} is not a Amstrong Number".format(Number))
