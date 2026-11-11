### Q. Python Program to Detect if Two Strings are Anagrams

str1 = input('Enter string : ')
str2 = input('Enter string : ')

if sorted(str1) == sorted(str2):
    print('Yes, Strings are Anagrams')
else:
    print('No, Strings are NOT Anagrams')