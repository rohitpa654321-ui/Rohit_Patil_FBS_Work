### Armstrong number detecting upto the limit value given by user

limit = int(input('Enter number : '))
# count = 0
# sum = 0
# num =0
# n = 0
print('Armstrong numbers in given range are :',end = ' ')
for i in range(0,limit+1):
    count = 0
    sum = 0
    temp = i
    while(temp>0):
        temp//=10
        count+=1
    # print(count)
    temp = i
    while (temp>0):
        r = temp%10
        temp//=10
        sum += r**count
    # print(sum)
    
    if(i == sum):
        print(i,end=' ')   










# while (n <= limit):

    
#     for i in range(0,limit):
#         temp = num
#         tem = temp
        
#         while (tem > 0):
#             tem = tem // 10
#             count +=1

#         while (temp>0):
#             r = temp%10
#             temp = temp // 10
    
#             sum = sum + (r**count)

#         if (sum == num):
#                 print(f'Armstrog number : {sum}')