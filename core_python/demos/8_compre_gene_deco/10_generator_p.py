### Generator uses yield insteaf of return

def numbers():
    print("Starting")

    for i in range(3):
        print("Producing", i)
        yield i                   # genarator pauses at yield 

g = numbers()

print("Generator created")


next(g)                   # next resume the function from where it stopped
next(g)
next(g)
# next(g)    # ERROR stopiteration (most recent call)

