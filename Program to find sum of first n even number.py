#program to find sum of first n even numbers

Number = int(input("Enter the Number : "))
Count=0
i=1
Sum = 0
while Count<Number:
    if i%2==0:
        Count=Count+1
        print(i)
        Sum=Sum+i
    i=i+1

print("Sum of first {} even number : {}".format(Number,Sum))
