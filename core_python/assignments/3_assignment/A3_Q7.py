## Write a program to check if user has entered a correct userid and password.
# stored user id and and password 

id = 'rohitpatil1001'
password = 'rg7675_1001'
pin = 83512
key = 712

# user input
user_id = input("Enter user ID : ")

if (user_id == id):
    user_pass = input('Enter password : ')
    
    if (user_pass == password):
        user_key = int(input('Enter key : '))
        
        if (user_key == key) :
            print('Login in successfully...')
            
        else:
            print('Invalid Credential !')
            
    elif (user_pass != password):
        user_pin = int(input('Enter user pin : '))
        
        if (user_pin == pin):
            user_key = int(input('Enter key : '))
            
            if (user_key == key):
                print('Login in successfully...')
                
            else:
                print('Invalid Credential !')
        
        else:
            print('Invalid Credential !')

        
    else:
        print('Invalid Credential !')

else:
    print('Invalid Credential')