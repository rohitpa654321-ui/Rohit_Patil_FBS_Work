### write a program to check if user has enter correct id and password.
### After verifying userid and password display a 4 digit random number and ask user to  enter the same.
### If user enter the same number then show him success message otherwise failed. (some like captch.)

import random

id = 'rohitpatil001'
password = 'rg76575'
captcha = random.randint(0000,9999)


user_id = input('Enter user ID : ')
user_pass = input('Enter password : ')
user_captcha = input('Enter captcha : ')

if (user_id == id and user_pass == password and user_captcha == captcha):
    
    print('you have successfully Login in...')

else:
    print('Failed to Login !')
    
