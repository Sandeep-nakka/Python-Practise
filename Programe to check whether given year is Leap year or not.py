#Programe to check whether given year is Leap year or not
Year=int(input("Enter the Year: "))
print(Year)
if (Year % 400 == 0) and (Year % 100 == 0):
    print("{} is a leap Year".format(Year))
elif (Year % 4 == 0) and (Year % 100 != 0):
    print("{} is a leap Year".format(Year))
else:
    print("{} is not a leap Year".format(Year))


#2000 = 0 0
#2004 = 0
#1900

#2000 - 100 century (00) - if century 400 - Leap Year

#year 4 - leap Year and that should not be a centrury
