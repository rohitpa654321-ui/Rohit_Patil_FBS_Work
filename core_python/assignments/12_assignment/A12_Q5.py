### Q. Python Program to Count the Number of Vowels in a String

str = input('Enter String : ')
count = 0

for i in str:
    if i in 'aeiouAEIOU':
        count +=1
        
print(f"Vowel Count : {count}")