### Write a program to print factorial of a number.

num = int(input('Enter number : '))

if (num<0):
    print('Not applicable')
    
else:
    fact = 1
    n = 0

    while ( n <= num):
        
        # for 0!
        
        if (n==0):
            print(f'1 * ',end =' ')
            n+=1
            
        # for last digit and factorial value
        if (n==num):
            fact*=n
            print(f'{n} = {fact}',end=' ')
            n+=1
            
        # for middle
        else:
            print(f'{n} * ',end=' ')
            fact*= n
            n+=1