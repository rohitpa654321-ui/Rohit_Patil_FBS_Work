from userdefineExp import RgException

def ShowEmp(id,name,age):
    try:
        if age<18 and age >79:
            raise RgException(age)
    except Exception as a:
        print(a)
    print(f"Id={id}\t Name={name}\t age={age}")

id=input("Enter Emp ID ")
name=input("Enter Emp Name ")
age=int(input("Enter EMp age "))
ShowEmp(id,name,age)