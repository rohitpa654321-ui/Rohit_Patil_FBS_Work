### WAP to accept an integer amount from user and tell minimum number notes needed
# to representing that amount.

# Take input 
amount = int(input('Enter amount : '))
temp = amount

# perform operation 
N500 = N200 = N100 = N50 = N20 = N10 = N5 = N2 = N1 = 0
if (temp >= 500 ):
    N500 = temp//500
    temp = temp%500
if (temp >= 200):
    N200 = temp //200
    temp = temp % 200
if (temp >= 100):
    N100 = temp // 100
    temp = temp % 100
if (temp >= 50):
    N50 = temp //50
    temp = temp %50
if (temp >= 20):
    N20 = temp //20
    temp = temp %20
if (temp >= 10):
    N10 = temp // 10
    temp = temp //10
if (temp >= 5):
    N5 = temp // 5
    temp = temp%5
if (temp >=2 ):
    N2 = temp//2
    temp = temp % 2
if (temp >= 1):
    N1 = temp // 1
    temp = temp % 1
else:
    print('invalid amount...')

notes = N500 + N200 + N100 + N50 + N20 + N10
coins =  N5 + N2 + N1
    
print(f'''notes needed :           500 = {N500}
                         200 = {N200} 
                         100 = {N100}
                         50  = {N50}
                         20  = {N20}
                         10  = {N10} 
                         5   = {N5}
                         2   = {N2}
                         1   = {N1}
                         
        total notes & coins  = {notes} & {coins}''')