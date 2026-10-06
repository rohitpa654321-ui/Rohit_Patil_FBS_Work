### exception class :

class RgException(Exception):
    def _init_(self,age):
        self.age=age

    def _str_(self):
        return f"{self.age} is not Eligibal"

ob=RgException(12)