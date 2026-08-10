### Function with passing parameter, without returning value.

#  function definition
def addition(num1,num2):
    
    sum = num1 + num2
    
    print(f'Addition of {num1} and {num2} is : {sum}')
    


x = int(input('Enter number 1 : '))
y = int(input('Enter number 2 : '))    

# function call
addition(x,y)