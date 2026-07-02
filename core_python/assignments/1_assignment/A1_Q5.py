### Write a program to enter P,T,R and calculate Compound Interest

# Take Input
p = 2796800
r = 24
t = 2
n = 1

# perform operation
CI = (p*(1+(24/100))**2) - p
final_a = p*(1+(r/100))**2

# Display result

print(f'Compound Interest is {CI} & Total amount is {final_a}')