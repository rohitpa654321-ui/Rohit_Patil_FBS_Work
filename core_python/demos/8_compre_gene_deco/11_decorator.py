### decorator

def decorator(fun):
    def wrapper():
        print("Before function call")
        fun()
        print("After function call")
    return wrapper

@decorator                # decorator allows you to add extra functionality...
def fun():
    print("I am from function")


fun()


print("\n\n****************************************************************************")
print("\n****************************************************************************\n\n")


def same(fun):    # we can change the name of function_name as the decorator
    def etc():
        print("Before function call")
        fun()
        print("After function call")
    return etc

@same           
def fun():
    print("I am from function")


fun()
