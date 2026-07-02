### convert temp from celsius to fahrenheit. (C/5 = (F-32)/9 )

# Take input
temp = (input('Enter temperature and af tertemp C (celsius)/F (fahrenheit)/K (kelvin) : '))

# Perform operation in condition
if ('C' in temp) :
    c = int(temp.replace('C',' '))
    print(f'Temp in fahrenheit is : {c*(9/5)+32} ॰F .')
    print(f'Temp in kelvin is : {c + 273.15} K .')

elif ('F' in temp):
    f = int(temp.replace('F',' '))
    print(f'Temp in celsius is : {(5/9)*(f-32)} ॰C .')
    print(f'Temp in kelvin is : {(5/9)(*f-32)+273.15} K .')

elif ('K' in temp):
    k = int(temp.replace('K',' '))
    print(f'temperature in celsius is : {k -273.15} ॰C .')
    print(f'Temperature in fahrenheit is : {(k-273.15)*9/5 +32} ॰F .')
    
else:
    print('Error, scan Temperature not detected...')