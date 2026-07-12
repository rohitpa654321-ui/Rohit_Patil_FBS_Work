### write a program to check if the number is palindrome or not
# (yes if num = 121 reverse = 121 )

# Take input
num = int(input('Enter number ( 3 digit) : '))
temp = num 

# perform operation
reverse = temp % 10 * 100
temp = temp // 10

reverse = reverse + temp % 10 *10
temp//=10

reverse = reverse + temp

print(f'The reverse of number is {reverse}')
if (num == reverse):
    print('Yes, this number is Palindrome number.')
else : print('Not a palindrome number. ')