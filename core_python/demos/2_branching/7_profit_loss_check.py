### Program to calculate and check profit or loss

cp = int(input('Enter cost price : '))
sp = int(input('Enter selling price : '))
amt = sp - cp
# condition operation
if (amt > 0):
    print(f'Your profit in this selling is nearly : {amt}rs.')
elif (amt == 0):
    print(f'Your profit in this selling is nearly zero it can be considered as loss too.')
else:
    print(f'Your loss in this selling is nearly : {amt}rs.')
    