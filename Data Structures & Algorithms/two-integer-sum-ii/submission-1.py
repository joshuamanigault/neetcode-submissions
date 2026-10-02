class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements =  {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in complements:
                return [complements[complement] + 1, i + 1]
            
            complements[num] = i
        