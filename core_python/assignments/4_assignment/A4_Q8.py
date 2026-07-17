### WAP to finf which numbers are divisible by 7 and multiple of 5 in given range

num1 = int(input('Enter range start from : '))
num2 = int(input('Enter range upto in between : '))
i = num1
temp = num1
while (num1 < num2):
    
    print('\nNumbers divisible by 7 are :',end =' ')
    while(i <= num2):
        if (i%7 == 0):
            print(i, end = ' ')
        i+=1
      
        
    print('\n\nNumbers divisible by 5 are : ',end = ' ')
    r = ''
    while(num1<=num2):
        if(num1%5 ==0):
            print(num1,end=' ')
        else: 
            r = f'{r}' + f' {num1}'
        num1+=1
    
    print(f'\n\nThis numbers are not divisible by 5 & 7 : {r}',end='')
    
    # print('\n\nThis numbers are not divisible by 5 & 7 : ',end = ' ')
    # while(temp <= num2):
    #     if((temp%5 !=0) and (temp%7 != 0)):
    #         print(temp,end = ' ')
        # temp+=1
    
    print('\n')
    num1 = num2