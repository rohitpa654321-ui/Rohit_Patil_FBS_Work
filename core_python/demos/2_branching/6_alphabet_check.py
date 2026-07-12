### program to check alphabet is vowel or consonant.

# Input
alpha = input('Enter alphabet : ')

# condition operation
if (alpha in 'aeiouAEIOU'):
    print(f"Alphabet '{alpha}' is vowel.")
elif (alpha in 'bcdfghjklmnpqurstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
    print(f"Alphabet '{alpha}' is consonant.")
else:
    print('Not a alphabet it can be a symbol or anything else.')