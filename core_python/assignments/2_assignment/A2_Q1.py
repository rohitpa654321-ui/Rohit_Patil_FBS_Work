### convert tthe time entered in hrs ,min and seconds into seconds

# Take input
time = int(input("Enter time (hhmmss) : "))
temp = time

# perform operation
# Hrs
hrs = temp // 10000
temp = temp % 10000
sec = hrs*60*60

# min
min = temp//100
temp = temp%100
sec = sec+ (min*60)

# sec
sec = sec + temp

# Display result
print(f'Time in seconds is : {sec} sec.')
