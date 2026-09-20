### Write a program to check if given number is a armstrong number or not.

# num = int(input('Enter number : '))
# temp = num

num = int(input('Enter number : '))

def armst(num, n =len(str(num))):
    
    if(num>0):
        d = num%10
        # num//=10
        return (d**n) + armst(num//10)
    else:
        return 0
    
def is_armst(num):
    sum = armst(num)
    if (sum == num):
        return 'Yes Armstrong number,'
    else:
        return 'NOT armstrong number.'
    
print(is_armst(num))