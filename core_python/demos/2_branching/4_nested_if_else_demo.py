### Marriage eligibility check
# Take input
gender = input('Enter gender (M/F) :')
age = input('Enter age :')

# operation on condition
if (gender == 'F'):
    if (age >= '18'):
        print('Girl is eligible for marriage.')
    else:
        print('Make Eligible first...')

if (gender == 'M'):
    if (age >= '21'):
        print('Boy is eligible for marriage.')
    else:
        balance = int(input('Bank balance of Boy (in Rs.) :'))
        if (balance >= 10000000):
            print('What needed more than this for marriage...')
        else:print('You have to be Eligible First and earn to take responsibilities...')
