### Write a progra to print all odd numbers until n.

num = int(input('Enter number : '))
n = 1

if (num <= 1):
    print('Not applicable number...!')

while(n<=num):
    if (n % 2 != 0):
        print(n)
    n += 1
    
    