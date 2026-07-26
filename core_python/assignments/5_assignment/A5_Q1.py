### Write a program to prompt user to enter userid and password.
# IF Id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times. After that program to terminate.


# Stored data by Admin or verifying team

user_id = 'rg1001'
password = 'Rohit@321'
n=4
 
for i in range(1,n):
    
    ID = input('Enter user id : ')
    pass_ = input('Enter pargssword : ')
    
    if (ID == user_id and password == pass_):
        print('Login in Successfully...')
        break
    
    else:
        print(f'Incorrect ID or Password please enter Valid Credential.({n-1-i} attempt remain)')
    
    
        
    