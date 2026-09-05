### Check whether the String is Palindrome or not...

str = input("Enter a string: ")
rev = ""
for ch in str:
    rev = ch + rev
print("Reversed string:", rev)
if rev == str:
    print("String is Palindrome")
else:
    print("String is not palindrome ")