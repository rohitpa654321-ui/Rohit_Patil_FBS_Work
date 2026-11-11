### importing Module :

# # 1. Direct import    :   
# import calculator1
# calculator1.add(25,45)   # call add function and perform operation as add fuction define...
# print(calculator1.add)    # it will give address of function add where it.s stored
# print(calculator1.abc)



# # 2. from module name import members.
# from calculator1 import sub

# a = int(input("Enter number1 : "))
# b = int(input("Enter number2 : "))

# sub(a,b)



# # 3. from module name import multiple members
# from calculator1 import sub,add,multi

# a=int(input("Enter the number1 : "))
# b=int(input("Enter the number2 : "))
# sub(a,b)
# add(a,b)
# multi(a,b)


# 4. from module name import all(*) :
from calculator1 import *

a=int(input("Enter the number1 : "))
b=int(input("Enter the number2 : "))
sub(a,b)
add(a,b)
multi(a,b)
print(abc)



import calculator1 as c 

a = int(input('Enter the number 1 : '))
b = int(input('Enter the number 2 : '))

c.add(a,b)