### WAP to print first n prime number.

n = int(input('Enter number (n) : '))

for i in range(2,n+1):
    
    flag = 1
    for j in range (2, i):
        if (i%j == 0):
            flag = 0
        
    if (flag):
        print(i)