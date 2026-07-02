### Marriage eligibility
# Take input
gender = input('Enter gender (M/F) :')
age = input('Enter age :')

# operation on condition
if (gender == 'F'):
    if (age >= '18'):
        print('Girl is eligible for marriage.')
    else:
        print('Pehele Bade ho jao...')

if (gender == 'M'):
    if (age >= '21'):
        print('Boy is eligible for marriage.')
    else:
        balance = int(input('bank balance kitna he (in Rs.) :'))
        if (balance >= 10000000):
            print('Marriage ke liye aur kya chahiye...')
        else:print('Phele kama lo...')
