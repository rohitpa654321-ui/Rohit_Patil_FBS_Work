### Indirect recursive function :
 
def fun_1():
    print('I am at first stage...')
    fun_2()                             # function calling another function

def fun_2():
    print('I am at second stage...')
    # fun_1()                              # function calling first function as indirect call
                                       # calling at infinite 
    
fun_1()                                  # function call