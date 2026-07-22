class MinStack:

    def __init__(self):
        self.minSt=[]
        

    def push(self, value: int) -> None:

        minVal=self.getMin()
        if minVal==None or minVal>value:
            minVal=value
        self.minSt.append([value,minVal])
        

    def pop(self) -> None:
        self.minSt.pop()
        return
        

    def top(self) -> int:
        return self.minSt[-1][0] if self.minSt else None
        

    def getMin(self) -> int:
        return self.minSt[-1][1] if self.minSt else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()