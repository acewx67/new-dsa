# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         ans = None
#         hs = {"+","-","*","/"}
#         for num in tokens:
#             if num not in hs:
#                 stack.append(int(num))
#             else:
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 ans = int(eval(f"{num1}{num}{num2}"))
#                 stack.append(ans)
#                 # print(ans)

#             # print(stack)
                
#         return stack.pop()

# same TC but less ms
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        
        return stack[-1]