### WAP to calculate the total salary of employee based on basic,
# DA = 10% of basic, TA =12% of basic, HRA = 15% of basic.

# Take input
basic = int(input('Enter basic salary of employee : '))

# perform operation

total_sal = basic + (basic*0.10) + (basic*0.12) + (basic*0.15)

# Display
print(f'Total salary of an employee is : {total_sal} rs.')