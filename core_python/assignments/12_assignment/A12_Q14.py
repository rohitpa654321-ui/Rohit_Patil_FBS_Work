### Q. Python Program to count the occurrences of each word in a string.

str = input('Enter String : ')

word = str.split()
occ_count = {}                # use dictionary first time I use list so error occurs

for i in word:
    if i not in occ_count:
        occ_count[i] = 1
    else:
        occ_count[i] += 1
        
for i in occ_count:
    print(f'{i} : ',occ_count[i])
    