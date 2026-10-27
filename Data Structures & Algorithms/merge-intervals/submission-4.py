class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        result = []
        i = 0 
        n = len(intervals)

        while i < n:
            start = intervals[i][0]
            max_end = intervals[i][1]
            j = i + 1
            while j < n and max_end >= intervals[j][0]:
                max_end = max(max_end, intervals[j][1])
                j += 1
            
            i = j
            result.append([start, max_end])


        return result
        