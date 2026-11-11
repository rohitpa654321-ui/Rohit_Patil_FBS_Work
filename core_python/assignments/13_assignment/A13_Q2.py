### Q. Python Program to Concatenate Two Dictionaries Into One.

dic1 = {
    'Vehicle' : 'Car',
    'Brand':'BMW'
}

dic2 = {
    'Model' : 'BMW M5',
    'Type'  : 'AWD Plug-in Hybrid'
}

# dic1.update(dic2)

print(dic1)



for i in dic2:
    dic1[i] = dic2[i]

print(dic1)