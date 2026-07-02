### Armstrong number detecting upto the limit value given by user

limit = int(input('Enter number : '))
count = 0
sum = 0
num =0
n = 0

while (n < limit):
    n+=1

    
    for i in range(0,limit):
        temp = num
        tem = temp
        
        while (tem > 0):
            tem = tem // 10
            count +=1

        while (temp>0):
            r = temp%10
            temp = temp // 10
    
            sum = sum + (r**count)

        if (sum == num):
                print(f'Armstrog number : {sum}')
               

        

    















# num = 1
# sum = 0
# count = 0
# cou = 0
# while (1):

    # num += 1
#     tem = num
#     temp = num
    
#     cou +=1
#     while (tem > 0 ):
#         tem = tem // 10
#         count +=1
#     print(count)
        
#     while (temp > 0):
#         r = temp % 10    
#         temp = temp //10
#         sum = sum + (r**count)
#         # print(sum)
#     print('.........')
#     # while (num <=159):
#     #     if (sum == num ):
#     #         print(num)
#     # break
        
        
    
    
    
    # while(temp > 0):
    #     r = temp % 10
    #     temp = temp//10
    #     sum = sum + r **count
        
    #     print(sum)