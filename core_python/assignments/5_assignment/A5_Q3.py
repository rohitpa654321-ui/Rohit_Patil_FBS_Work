###  Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition :  
# a. Children below 12 = 30% discount  
# b. Senior citizen (above 59) = 50% discount  
# c. Others need to pay full.  

n = int(input('Enter number of passengers : '))
amount = 0
for i in range(1, n+1):
    cost = int(input('Enter cost as per stop ticket : '))
    age = int(input('Enter age : '))
      
    if (age>0 and age<130): 
        if (age < 12):
            cost = cost/100*70
        elif (age > 59):
            cost = cost/2
    else:
        print('Invalid age...')
        break
    
    amount += cost
else:
    print(f'Total amount : {amount}')
