class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                cTemp, cIdx = stack.pop()
                result[cIdx] = i - cIdx

            stack.append((t, i))

        return result
        
            