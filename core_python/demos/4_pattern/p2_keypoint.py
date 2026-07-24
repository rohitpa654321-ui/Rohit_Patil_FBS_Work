### PATTERN differes with values

# 1) outer loop (i) for rows
# 2) inner loop (j) for columns
# 3) similar value in row use i
# 4) value diferes in row use j 


# similar values in row - use i

for i in range(1,6):
    for j in range(1,6):
        print(i,end = ' ')
    print()


print()
# different values in rows - use j
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
    
    