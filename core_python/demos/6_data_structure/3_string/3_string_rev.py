### Write a program to reverse the string...

str = input("Enter a string: ")
rev = ""
for ch in str:
    rev = ch + rev
print("Reversed string:", rev)

