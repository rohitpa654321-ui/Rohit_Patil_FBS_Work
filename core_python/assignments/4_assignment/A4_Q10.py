### WAP to check if given number is Perfect Number.

num = int(input('Enter Number : '))
n = 1
i = 0
while (n<num):
    
    
    if (num%n ==0):
        i += n
    n+=1

if (num == i):
    print(f'{num} is a perfect number.')
    
else:
    print(f'{num} is NOT a perfect number.')
    
