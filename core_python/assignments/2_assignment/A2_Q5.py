### WAP to calculate the selling price of book based on cost price and discount . 

# Take input
cp = int(input('Enter cost price of books( in rs.) : '))
dis = int(input('Enter discount percentage : '))

# operation 
sp = cp - (cp/100*dis)

print(sp)