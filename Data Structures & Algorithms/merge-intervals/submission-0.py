class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [x, y] - current intervals
        [n, m] - following intervals

        if y >= the n of the following elements, continue the interval
        When this condition no longer fulfills, 
        the new interval will be: [x, m]

        otherwise, append the interval to the resulting array

        intervals array must sorted based on the starting interval element
        """

        result = []
        intervals = sorted(intervals, key = lambda x: x[0])
        n = len(intervals)

        i = 0
        while i < n:
            start = intervals[i][0]
            max_end = intervals[i][1]
            j = i + 1
            while j < n and max_end >= intervals[j][0]:
                max_end = max(max_end, intervals[j][1])
                j += 1
            
            result.append([start, max_end])
            i = j 

        
        return result