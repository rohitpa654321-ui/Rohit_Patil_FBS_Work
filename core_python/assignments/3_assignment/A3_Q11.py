### Accept age of five people and also per person ticket amount and then calculate
### total amount to ticket to travel for all of them based on following condition.
# a. Childern below 12 - 30% discount.
# b. Senior citizens (above 59) - 50% discount.
# c. Others need to pay full.

# 1st person

p1_age = int(input('Enter age of 1st person : '))
cost = int(input('Enter cost of destination : '))
if (p1_age<0):
    print('Invalid')
else:
    if (p1_age<12):
        p1 = cost/100 * 70
    elif (p1_age >59):
        p1 = cost/100*50   # p1 = cost/2
    else:
       p1 = cost

# 2nd person

p2_age = int(input('Enter age of 2nd person : '))
cost = int(input('Enter cost of destinaion : '))

if (p2_age <0):
    print('Invalid')
else:
    if (p2_age<12):
        p2 = cost/100*70
    elif (p2_age >59):
        p2 = cost/100 * 50
    else:
        p2 = cost

# 3rd person
        
p3_age = int(input('Enter age of 3rd person : '))
cost = int(input('Enter cost of destination : '))

if (p3_age<0):
    print('Invalid')
else:
    if (p3_age < 12):
        p3 = cost/100*70
    elif (p3_age > 59):
        p3 = cost/2
    else:
        p3 = cost

# 4th person

p4_age = int(input('Enter age of 4th person : '))
cost = int(input('Enter cost of destination : '))

if (p4_age<0):
    print('Invalid')
else:
    if (p4_age < 12):
        p4 = cost/100*70
    elif (p3_age > 59):
        p4 = cost/2
    else:
        p4 = cost

# 5th person 

p5_age = int(input('Enter age of 5th person : '))
cost = int(input('Enter cost of destination : '))

if (p5_age<0):
    print('Invalid')
else:
    if (p5_age < 12):
        p5 = cost/100*70
    elif (p5_age > 59):
        p5 = cost/2
    else:
        p5 = cost
        
total_fare = p1+p2+p3+p4+p5

print()
print('1st Person ticket price : ',p1)
print('2nd Person ticket price : ',p2)
print('3rd Person ticket price : ',p3)
print('4th Person ticket price : ',p4)
print('5th Person ticket price : ',p5)

print()
print('Total cost : ',total_fare)