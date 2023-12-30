#Write a Programe to count the number of vowels and consonants in a string ( Pass the string from console)

input_String= input("Enter the String : ")
input_String = input_String.lower()
#print(input_String)
input_String=input_String.replace(" ","")
#print(input_String)
i =0
vowels =0
Consonants =0
while i<len(input_String):
    if input_String[i] == 'a' or input_String[i] == 'e' or input_String[i] == 'i' or input_String[i] == 'o' or input_String[i] == 'u':
        vowels = vowels+1
    else:
        Consonants=Consonants+1
    i=i+1

print("Vowels count: {}".format(vowels))
print("Consonants count: {}".format(Consonants))


vowels =0
Consonants =0

for j in input_String:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        vowels = vowels+1
    else:
        Consonants=Consonants+1
print("For Loop Vowels count: {}".format(vowels))
print("For Loop Consonants count: {}".format(Consonants))


vowels =0
Consonants =0

for i in range (0,len(input_String)):
    if input_String[i] == 'a' or input_String[i] == 'e' or input_String[i] == 'i' or input_String[i] == 'o' or input_String[i] == 'u':
        vowels = vowels+1
    else:
        Consonants=Consonants+1
print("For range Loop Vowels count: {}".format(vowels))
print("For range Loop Consonants count: {}".format(Consonants))
