class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        result = 0

        for num in numbers:
            if num - 1 not in numbers:
                length = 1 

                while num + 1 in numbers:
                    length += 1
                    num += 1
                
                result = max(result, length)
        return result

        