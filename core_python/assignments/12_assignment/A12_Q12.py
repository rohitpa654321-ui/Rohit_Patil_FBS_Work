### Q. Python Program to count number of lowercase characters in a string.

str = input('Enter String : ')
count = 0

for i in str:
    if i.islower():
        count+=1
        
print(f'Lowercase Count : {count}')
