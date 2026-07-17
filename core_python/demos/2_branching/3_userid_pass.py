### program to Login with correct Id and Password

# Stored data
user_Id = '2122rg'
password = '2121'

# Take input
Id = input('Enter user Id :')
pass_Id = input('Enter password :')

# operation on condition
if (user_Id == Id and password == pass_Id):
    print('Login in successfully...')
    
else :
    print('Invalid Credential...')
