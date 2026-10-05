class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for p in s:
            if p in mapping:
                opening = mapping[p]
                if not stack or stack.pop() != opening:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0

    