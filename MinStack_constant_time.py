class MinStack:

    def __init__(self):
        self.items=[]
        self.supporting=[]
        

    def push(self, x: int) -> None:
        if len(self.supporting)==0:
            self.supporting.append(x)
        elif x <= self.supporting[-1] and len(self.supporting)>0:
            self.supporting.append(x)
        self.items.append(x)
            
        
    def pop(self) -> None:
        if self.supporting[-1]==self.items[-1]:
            self.supporting.pop()
            return self.items.pop()
        else:
            return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.supporting[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()