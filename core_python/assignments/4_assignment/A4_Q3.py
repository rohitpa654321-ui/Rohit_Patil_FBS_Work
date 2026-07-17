### Write a program to print sum of series upto n.

num = int(input('Enter number : '))
sum = 0
n = 1

while(n <= num):
    if (n == num):
        sum+=n
        print(f'{n} = {sum}')
        n+=1
    else:
        print(f'{n} +',end = ' ')
        sum+=n
        n+=1
    