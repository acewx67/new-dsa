# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.index = None

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.index is None:
#             self.index = 0
#         else:
#             self.index += 1

#     def pop(self) -> None:
#         self.stack.pop()
#         self.index -= 1

#     def top(self) -> int:
#         return self.stack[self.index]

#     def getMin(self) -> int:
#         return min(self.stack[:self.index+1])

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]