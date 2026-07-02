### Write a program to check if person is eligible to marry or not.(male 21+ and female 18+)

print(' Check whether the person is eligible to marry or not...')

name_m = input('Enter first and last name of male partner : ')
age_m = int(input('Enter age : '))

name_f = input('Enter first and last name of femal partner : ')
age_f = int(input('Enter age : '))

if (age_m >100 or age_f > 100):
    print('Abto rukhjao ..., ye umar shadi ki nahi ye sab yaha nahi hota...')

if (age_m > 20):
    print(f'{name_m} is eligible to marry.')
else:
    print(f'{name_m} is not eligible to marry.')
if (age_f > 17):
    print(f'{name_f} is eligible to marry.')
else:
    print(f'{name_f} is not eligible to marry.')

if (age_m > 20 and age_f > 17):
    print('''Both partners are mature to make decision and eligible for marriage...
          This marriage will be valid if done...''')
else:
    print('''This marriage is not valid...
          bade ho ja beta teri shaadi karunga.🎶..''')



# remiander for code is remain