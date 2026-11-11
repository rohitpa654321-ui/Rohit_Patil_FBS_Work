### File Handling in Python

# modes : "r" - read, "w" - write, "a" - append, "r+" - read and write, "w+" - write and read, "a+" - append and read

# binary modes : Used for non-text files like images, audio files, etc. The modes are:
#               
#               "rb" - read binary, "wb" - write binary, "ab" - append binary, "rb+" - read and write binary,
#               "wb+" - write and read binary, "ab+" - append and read binary




file = open("11_file_handling/data.txt", 'r+')
print(file.read())
print(file.tell())
print(file.seek(0))
print(file.readline())
print(file.readlines())
print(file.name)
print(file.mode)
file.close()
print(file.closed)

print("\n..............................................................................................\n\n")

with open("11_file_handling/data1.txt",'w+', encoding = 'utf-8+') as data:
    data.write("Hello, World!")
    data.writelines(["\nhello it's me", "\n hello it's you", "\nhello it's them"])
    data.seek(0)
    print(data.read())
    
print(data.closed)