### Q. Python Program to Multiply All the Items in a Dictionary.

dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

mult = 1

for i in dic:
    mult = mult * dic[i]
    
print(f'Multiplication of Items of Dictionary : {mult}')