### Write a program to check if number is a palindrome or not.

def palindromeCheck(num):
    temp = num
    rev = 0
    while(temp>0):
        r = temp%10
        temp//=10
        rev = rev*10+ r
    if (rev==num):
        return 'Number is a Palindrome number'
    else:
        return 'Number is NOT Palindrome number'
    
print(palindromeCheck(int(input('Enter number : '))))

