### write a program to check if the number is palindrome or not
# (yes if num = 121 reverse = 121 )

# Take input
num = int(input('Enter number ( 3 digit) : '))

# perform operation
last = num % 10
first = num // 100
mid  = (num//10) % 10

print(f'The reverse of number is {last}{mid}{first}')
if (last == first):
    print('Yes, this number is Palindrome number.')
else : print('Not a palindrome number. ')