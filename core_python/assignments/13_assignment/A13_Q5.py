### Q.  Python Program to Sum All the Items in a Dictionary.

dic = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
    6: 36,
    7: 49,
    8: 64,
    9: 81
    }

sum = 0
# for i in dic.values():
#    sum = sum + i


for i in dic:
    sum = sum + dic[i]
    
print(f'Sum Of Items : {sum}')

