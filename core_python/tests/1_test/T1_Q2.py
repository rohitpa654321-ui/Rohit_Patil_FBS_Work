### Write a program to calculate simple interest based on principal, Rate, Time (SI = P*R*T/100)
 
# Take Input 
P = int(input('Enter principal amount :'))
R = int(input('Enter rate of interest :'))
T = int(input('Enter Time period in year :'))

# perform operation

SI = P*R*T/100
Final_A = SI + P

# Display
print(f'Simple interest is : {SI}rs.\
        Final amount is {Final_A}rs.')