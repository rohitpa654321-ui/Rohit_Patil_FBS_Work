### WAP to check if a given number is prime number or not. OR print all prime in between 

num = int(input('Enter number : '))

n = 2

while(n<=num):
    
    i = 2
    flag = 1
    
    while(i<n):
        if (n%i == 0):
            flag = 0
        i+=1
        
    if (flag):
        print(n)
    n+=1















# num =int(input('Enter number : '))
# n=2
# i=2
# flag=0

# # if(num>1):
# #     print(n)

# while(n<num):
#     while(i<n):
#         # if(n==2):
#         #     print(n)
#         #     i+=1
#         #     n+=1
            
#         if (n%i==0):
#             flag=1
#             
#     i+=1
    
#     if(flag==0):
#         print(n)

# n+=1
