### Q. Python Program to Remove the Given Key from a Dictionary.

dic = {
    'vehicle' : 'Car',
    'brand':'BMW',
    'model' : 'M5',
    'type'  : 'AWD Plug-in Hybrid'
}

key = input('Enter key : ')
# dic.pop(key)

if key in dic:
    del dic[key]
else:
    print('Not Found') 

print(dic)
