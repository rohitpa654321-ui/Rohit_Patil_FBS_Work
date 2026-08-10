### Palindrome
def isPalindrome(num):
    temp = num
    rev = 0
    while(temp>0):
        d = temp%10
        temp = temp //10
        rev = rev*10 + d
    
    if (rev == num):
        return True
    else:
        return False
    
num = int(input('Enter number : '))
res = isPalindrome(num)
print(res)
