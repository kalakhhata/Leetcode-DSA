class MyQueue(object):

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack_out)!=0:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack_out)!=0:
            return self.stack_out[-1]
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_in)==len(self.stack_out)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()