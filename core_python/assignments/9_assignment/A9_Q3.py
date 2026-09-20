### Write a program to reverse a given number using recursive fuction.

def reverseNum(num,r=0):
    
    if (num>0):
        return reverseNum( num//10 , (r*10)+num%10)
    
    else:
        return r

print('Reverse number : ',reverseNum(int(input('Enter number : '))))