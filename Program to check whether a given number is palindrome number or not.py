#Program to check whether a given number is palindrome number or not
number=int(input("Enter the Number: "))
num=number
rev_num=0
while num>0:
    rev_num=(rev_num *10)+(num%10)
    num=num//10
if number == rev_num:
    print("Number {} is a Palindrome".format(number))
else:
    print("Number {} is not a Palindrome".format(number))
