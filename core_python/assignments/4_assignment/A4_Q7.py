### WAP to print all integers upto n that aren’t divisible by 2 and 3.
num = int(input('Enter number : ' ))
n = 1


while (n < num):
    
    if ((n%2 !=0)and n%3!=0):
        print(n)
        
    n+=1