### Exception in file handling

# 1. FileNotFoundError : This exception is raised when trying to open a file that does not exist.

# 2. IOError / io.UnsupportedOperation : This exception is raised when an I/O operation (like reading or writing) fails for an I/O-related reason.

# 3. FileExistsError : This exception is raised when trying to create a file that already exists.



try:
    with open("data3.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")
    
    

try:
    with open("data.txt", "r") as file:
        print(file.write('As I am writing this, I am thinking about the future.'))
except IOError:
    print("An I/O error occurred while unsupported mode is used.")



try:
    with open("data.txt", "x") as file:
        file.write("Hello, World!")
    
except FileExistsError:
    print("File already exists.")

