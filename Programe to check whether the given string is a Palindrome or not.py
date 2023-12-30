#Programe to check whether the given string is a Palindrome or not

#MADAM

s1=input("Enter the String: ")
#s2=s1[::-1]
if s1==s1[::-1]:
    print("String {} is a Palindrome".format(s1))
else:
    print("String {} is not a Palindrome".format(s1))
