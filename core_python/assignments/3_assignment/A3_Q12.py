### Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter number 3 digit number : '))
temp = num 
reverse = 0

if (temp > 99 and temp < 999):
    if (temp > 0):
        r = temp%10
        temp = temp//10
        reverse = reverse + r*100
        if (temp>0):
            r = temp%10
            temp = temp//10
            reverse = reverse + r*10
            if(temp>0):
                r = temp%10
                temp = temp//10
                reverse = reverse + r
                
            if (reverse == num):
                print(f'{num} is a Palindrome number.')
            else:
                print('Not a Palindrome number.')
                
else:
    print('Invalid number...!')
    