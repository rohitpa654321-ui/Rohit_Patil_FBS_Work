### wAP to calculate the selling price of books based on cost price and discount .

book = input('''
        list of books and discount by goverment for students

         1. english gr......... = 257rs. (55%)
         2. maths lab.......... = 425rs. (75%)
         3. science world...... = 235rs. (52%)
         4. harmony within you. = 250rs. (80%) 
         5. hindu darm ka gyan. = 1200rs.(95%)
      
      Enter serial number of above book to choose (1,4,5) : ''')
price = 0
if ('1' in book):
    price = 257 - (257/100 * 55)
if ('2' in book):
    price = price + 425 - (425/100*75)
if ('3' in book):
    price = price + 235 - (235/100*52)
if ('4' in book):
    price = price + 320 - (250/100*80)
if ('5' in book) :
    price += price + 1200-(1200/100*95)
    
if (',' in book):
    print(f'Your total amount of books is : {price} rs.')
    
else:
    print('invalid books.')