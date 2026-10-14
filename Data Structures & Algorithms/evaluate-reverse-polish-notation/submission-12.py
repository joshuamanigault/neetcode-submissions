class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '-':
                right_hand = stack.pop()
                left_hand = stack.pop()
                stack.append(left_hand - right_hand)
            elif t == '/':
                right_hand = stack.pop()
                left_hand = stack.pop()
                stack.append(int(left_hand / right_hand))
            else:
                stack.append(int(t))
                
        return stack[-1]