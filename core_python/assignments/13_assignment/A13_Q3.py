### Q. Python Program to Check if a Given Key Exists in a Dictionary or Not.


dic = {
    'Vehicle' : 'Car',
    'Brand':'BMW',
    'Model' : 'M5',
    'Type'  : 'AWD Plug-in Hybrid'
}

key = input("Enter key : ")

if key in dic:
    print('Key found')
else:
    print('Not found')