

class Solution:
    # Write your code here
    def __init__(self):
        super().__init__()
        self.stack = []
        self.queue = []
    
    def pushCharacter(self,a):
        self.stack.append(a)
    
    def enqueueCharacter(self,a):
        self.queue.append(a)
    
    def popCharacter(self):
        return self.stack.pop()
        
    def dequeueCharacter(self):
        return self.queue.pop(0)
    

