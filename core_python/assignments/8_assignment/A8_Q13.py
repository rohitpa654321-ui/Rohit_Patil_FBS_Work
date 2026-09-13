### Write a program to check if given number is an Armstrong number or not.
# For each task create seperate functions.

def sepCount(num):
    count=0
    while(num>0):
        num//=10
        count+=1
    return count

def armstrongSum(num):
    count = sepCount(num)
    sum = 0
    while(num>0):
        r = num%10
        num //=10
        sum+= r**count
    return sum

def armScheck(num):
    sum = armstrongSum(num)
    
    if (sum == num):
        return 'Yes Armstrong number'
    else:
        return 'NOT armstrong number'
    
print(armScheck(int(input('Enter number : '))))