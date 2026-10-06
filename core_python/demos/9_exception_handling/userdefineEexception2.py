### user define exception without class :


try :
    age=int(input("Enter the AGE : "))
    if age<18:
        raise Exception("Not Eligible ")
except Exception as e:
    print(e)
print("AGE check ")
12