### Write a program to print prime number between 1 to 100.

n = int(input('Enter lower limit : '))
m = int(input('Enter upper limit : '))

for i in range(n,m+1):
    
    flag = 1
        
    for j in range(2, i):
        if (i%j ==0):
            flag = 0
    if(flag):
        print(i)
        
    