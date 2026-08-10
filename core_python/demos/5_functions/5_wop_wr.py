### Function without passing parameter, with returning value.

#  function definition
def addition():
    
    num1 = int(input('Enter number 1 : '))
    num2 = int(input('Enter number 2 : '))
    
    sum = num1 + num2
    
    return sum


# function call
print(f'Addition is : {addition()}')