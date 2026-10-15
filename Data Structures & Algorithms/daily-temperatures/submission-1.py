class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [(30, 0)]
        []
        """
        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            curr_temp = temperatures[i]
            while stack and curr_temp > stack[-1][0]:
                t_tuple = stack.pop()
                idx = t_tuple[-1]
                result[idx] = i - idx   

            stack.append((curr_temp, i))
        
        return result