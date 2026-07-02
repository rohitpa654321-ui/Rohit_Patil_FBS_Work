### WAP to calculate profit and loss.

# Take input
cp = int(input('Enter cost price (rs.) : '))
sp = int(input('Enter selling price (rs.) : '))

amt = sp - cp

# operation with condition
if (amt > 0):
    print(f'{amt} rs. is your profit in this selling.')
elif (amt == 0):
    print(f'Your profit is {amt} in this selling, It can be considered as loss.')
# elif (amt <= 0):
    # print(f'{amt} rs. is your loss in this selling.')
else:
    print(f'{amt} rs. is your loss in this selling.')
