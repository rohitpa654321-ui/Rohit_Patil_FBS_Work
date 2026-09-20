### Q. Write a program to reverse a number using recursion.

def reverseNum(num,rev = 0 ):
    
    if num == 0:
        return rev
    else:
        d = num % 10
        rev = rev*10 + d     
        
        return reverseNum(num//10,rev)
        
res = reverseNum(int(input('Enter number : ')))

print(res)