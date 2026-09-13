### Write a program to find sum of digit of a number.

def digSum(num):
    sum = 0
    while(num>0):
        
        r = num%10
        num = num//10
        sum+=r
        print(r)
    return sum

print(f'Sum of digits of a number : {digSum(int(input('Enter number : ')))}')
