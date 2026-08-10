### Varialble length Argument concept : (*) asterisk symbol
# used to pass multiple parameters
# stored in typle form


def add(*num):
    sum = 0
     
    for val in num :
        sum+=val
        
    return sum

res = add(10,20,30,40,50)
print('Addition is : ',res)