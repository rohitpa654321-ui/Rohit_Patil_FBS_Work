### Default Parameter.

def emp(id, name, sal =0, dept = 'Admin'):
    print('ID:',id)
    print('NAME:', name)
    print('SALARY', sal)
    print('DEPARTMENT:',dept)
    
emp(101,'ABC', 35000, 'IT')
print('\n#####################\n')
emp(102,'XYZ', 5000)