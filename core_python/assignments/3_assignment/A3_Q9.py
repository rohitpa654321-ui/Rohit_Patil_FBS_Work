### Input 5 subjects marks from user and display grades.

print('Enter marks of subjects...')

m1 = int(input('English : '))
m2 = int(input('Maths : '))
m3 = int(input('Marathi : '))
m4 = int(input('Science : '))
m5 = int(input('Social Science : '))
m6 = int(input('Information Technology : '))

if (m1<= 100 and m2<= 100 and m3<= 100 and m4<= 100 and m5<= 100 and m6<=100 and m1>=0 and m2>=0 and m3>=0 and m4>=0 and m5>=0 and m6>=0 ):

    print('IT is optional subject percentage : ', m6/100*100)

    percent = (m1+m2+m3+m4+m5)/500*100
    
    if (percent > 95):
        print(' Grade : A1+')
    elif (percent >= 90 and percent < 96):
        print('Grade : A+')
    elif (percent >=80 and percent < 90):
        print('Grade : A')
    elif (percent >=65 and percent < 80):
        print('Grade : B')
    elif (percent >= 50 and percent < 65):
        print('Grade : C')
    elif (percent >= 35 and percent < 65):
        print('Grade : D')
    else:
        print('fail')
    # print (percent)
else:
    print('Invalid marks')