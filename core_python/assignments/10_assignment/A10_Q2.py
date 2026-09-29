### Q. Write a program to find maximum and minimum element in a list.


li = [10,20,30,50,90,30,40,60]

max = li[0]
min = li[0]

for i in li:
    if max < i:
        max = i
    if min > i:
        min = i
    
print(f'Max = {max}\nMin = {min}')