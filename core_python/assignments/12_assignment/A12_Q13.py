### Q. Python Program to count number of digits and letters in a string.

str = 'Rohit_Patil_123987'
dig = 0
let = 0

for i in str:
    if i.isalpha():
        let += 1
        
for i in str:
    if i.isdigit():
        dig += 1

print(f'Letters : {let}', f'Digits : {dig}', sep = '\n' )