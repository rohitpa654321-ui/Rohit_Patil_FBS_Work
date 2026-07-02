### WAP to input any alphabet and check whether it is vowel or consonant.

# Take input 
alpha = input('Enter alphabet : ')

# operation with condition
if (alpha in 'aeiouAEIOU'):
    print(f'Alphabet {alpha} is an vowel.')
elif (alpha in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'):
    print(f'Alphabet {alpha} is a consonant.')
else:
    print('Input is not an alphabet it can be any symbol.')
