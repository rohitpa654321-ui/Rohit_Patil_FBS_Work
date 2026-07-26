### Enter number of students from user. For those many student accept marks of 5 
# subject marks from user and calculate percentage. Display all percentage and 
# Average percentage of students

n = int(input('Enter number of Students : '))
perc = 0
for i in range(1, n+1):
    m = 0
    percentage =0
    # suffix = {1: 'st',2:'nd',3:'rd'} # just trying 

    
    for j in range(1,6):
        marks = int(input(f"Enter marks {j}{'st' if j==1 else 'nd' if j==2 else 'rd' if j==3 else 'th'} : "))
        m+=marks
    percentage = m/500 *100
    print(percentage)
    perc += percentage
average_per = perc/ n
print('Average percentage of Stidents : ',average_per)
