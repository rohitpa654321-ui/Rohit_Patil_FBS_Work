### Lambda function : addition of numbers

add = lambda num1,num2 : num1+num2
res = add(21,48)                        # variable add is use as function to reuse
print(res)


### If function assign to any variable it is also call as a function

def add(num1,num2):
    sum = num1+num2
    
    return sum

fun1 = add           # add function assign to variable

print(fun1(21,48))        # variable use as function


print(add(50,40))