### Distructor : __del__()method 
# auto call --- object is about to distroyed.

class FileManager:
    def __init__(self):
        self.file = open("data.txt", "w")   # creating file and open to write
        print("File opened") 

    def __del__(self):             # distuctor define and automatically called
        self.file.close()          # Cleanup or close operation 
        print("File closed")       

f = FileManager()               # automatically call distructor
                                # operation before object deletion
del f                          # final deleted object witch is created and closed
