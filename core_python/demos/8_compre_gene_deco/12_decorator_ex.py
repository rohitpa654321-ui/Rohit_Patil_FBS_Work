### Outer and inner function calling  :

def outerfun():
    name ="FBS"
    print("outer...")
    def innerfun():
        print(name)
    return innerfun
# a=outerfun()
# print("++
# a()
outerfun()