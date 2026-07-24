### pattern : 

#   A A A A A
#   B B B B B
#   C C C C C 
#   D D D D D
#   E E E E E


for i in range(1,6):
    for j in range(1,6):
        print(chr(64+i), end = ' ')
    print()
    
    
# used ASCII code / Unicode  

# 1) chr()  : chr(65)  # using unicode gives character
# 2) ord()  : ord(A)   # input character gives unicode for that char

