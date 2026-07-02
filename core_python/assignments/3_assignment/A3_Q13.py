### Write a programe to input electricity unit charges and calculate total electricity bill
### according to given condition...
# For first 50 units rs. 0.50/unit
# For next 100 units rs. 3.75/unit
# For next 100 units rs. 6.20/unit
# For above 250 unit rs. 7.50/unit
# An additional surcharge of 20% is added to the bill

units = int(input('Enter consumption number of units : '))
total_bill = 0


if (units > 250):
    total_bill = total_bill + (units - 250)* 7.50
    units = units - (units - 250) 
if (units > 150):
    total_bill = total_bill + (units - 150)*6.20
    units = units - (units-150)
if (units > 50):
    total_bill = total_bill + (units - 50)*3.75
    units = units - (units - 50)
if (units > 0): 
    total_bill = total_bill + units*0.5

else:
    total_bill = 0
    
total_bill = total_bill + (total_bill/100*20)

print(f'Your Total Bill to pay : {total_bill} rs.')
