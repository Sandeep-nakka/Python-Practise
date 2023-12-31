#program to find reverse of a given number
number=int(input("Enter the Number: "))
num=number
rev_num=0
while num>0:
    rev_num=(rev_num *10)+(num%10)
    num=num//10
print("Reverse Number of {} number : {}".format(number,rev_num))
