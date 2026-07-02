### WAP to reverse three digit number . 

# Take input 

num = int(input('Enter three digit nummber : '))
temp = num

# perform operation 
if (num //1000 == 0):
    r = temp %10 *100
    temp = temp//10
    r = r + (temp %10)*10
    temp = temp//10
    r = r + temp
    
    print(f'reverse of three digit is : {r}')
    