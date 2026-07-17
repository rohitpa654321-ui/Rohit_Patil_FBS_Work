### WAP to print all numbers in a range divisible by a given number.

num1 = int(input('Range starts from :'))
num2 = int(input('Range ends to : '))
n = int(input('Enter number as divisor : '))

print(f'Numbers divisible by {n} are : ',end= ' ')
while (num1 <= num2):
    if (num1%n==0):
        print(num1,end=' ')
    num1+=1