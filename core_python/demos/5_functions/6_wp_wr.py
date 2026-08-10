### Function with passing parameter, with returning value.

#  function definition
def addition(num1,num2):
    
    sum = num1 + num2
    return sum


x = int(input('Enter number 1 : '))
y = int(input('Enter number 2 : '))    

# function call
print(f'Addition is : {addition(x,y)}')