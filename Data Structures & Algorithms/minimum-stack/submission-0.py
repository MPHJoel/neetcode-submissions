class MinStack:

    def __init__(self):
        self.stack = []
        # tuple: 1st element is value, second is min

    def push(self, val: int) -> None:
        if len(self.stack) != 0:
            minimum = min(self.stack[-1][1],val)
        else: 
            minimum = val
        self.stack.append((val,minimum))
        

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
