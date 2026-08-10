### Variable length keyword argument concept :
# 2 asterisk symbol before parameter name(**)
# used to pass value with it's keyword
# stored in dictionary form

def emp(**data):
    print(type(data))
    
    for key,val in data.items():
        print(f'{key}={val}')
    
    
emp(id = 101, name = 'Rohit', sal = 150000, dept = 'IT')