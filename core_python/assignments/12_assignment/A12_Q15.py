### Q. Python Program to find larger string without using built-in functions.


str1 = input('Enter string 1 :')
str2 = input('Enter string 2 :')
count1 = 0
count2 = 0

for i in str1:
    count1+=1
    
for j in str2:
    count2+=1

if count1 > count2 :
    print(f"Larger String is : {str1}")
elif count1 < count2 :
    print(f"Larger String is : {str2}")
else:
    print('Both strings are equal')