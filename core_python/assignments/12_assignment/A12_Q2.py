### Q. Python Program to Remove the nth Index Character from a Non-Empty String

str = 'I am Happy and fittest healthy person'
n = int(input("Enter index number : "))

new = str[:n] + str[n+1:]

print(new)