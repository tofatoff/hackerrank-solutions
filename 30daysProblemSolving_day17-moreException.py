#Write your code here
class Calculator:
    def __init__(self):
        super().__init__()
        
    def power(self,n,p):
        if n >= 0 and p >= 0:
            return n**p
        else:
            raise Exception("n and p should be non-negative")

