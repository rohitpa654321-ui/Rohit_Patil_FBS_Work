### Write a program to find sum of digits using recursive function.


def reverseNum(num):
    rev = 0
    if (num>0):
        r = (num%10)
        num =num//10
        return r + (reverseNum(num))
    
    else:
        return 0
    
    
print('Sum of digits is : ',reverseNum(int(input('Enter number : '))))
