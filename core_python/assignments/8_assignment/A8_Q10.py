### Write a program to find reverse of a number.

def revNum(num):
    rev = 0
    while(num>0):
        r = num%10
        num = num//10
        rev = rev*10 + r
        
    return rev

print(f'reverse of number is : {revNum(int(input('Enter number : ')))}')
