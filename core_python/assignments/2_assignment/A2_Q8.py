### WAP to swap two numbers using third variable.

# take two numbers

a = int(input('Enter a : '))
b = int(input('Enter b : '))

# perform swaping operation
c = b
b = a
a = c

# Display 
print(f'a = {a} and b = {b} .')