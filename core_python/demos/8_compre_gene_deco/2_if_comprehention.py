# example
# li=[]
# for i in range(1,101):
#     if i%2 != 0:
#         li.append(i)
# print('Traditional loop = ',li)

li=[i for i in range(1,101) if i%2 != 0]
print('odd nums : ',li)



### firstbit ---- FIRSTBIT

s = 'firstbit'
# print(s.upper())

res = [i.upper() for i in s]
print('UpperCase = ',res)
