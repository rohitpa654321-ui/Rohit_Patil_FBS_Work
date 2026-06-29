
### Write a program to enter the P,R,T and  calculate the simple interest.

# Take input
p = 2796800  
r = 24     # it is in percent it can be convert to 24/100
t = 2      # time period is in years

# perform operation
SI = p*r/100*t
final_a = SI + p

# Display result
print(f'The simple interest is : {SI} rs. ')
print(f'Final amount (A+SI) is : {final_a} rs.')