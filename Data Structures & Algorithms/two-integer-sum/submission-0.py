class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            
            hash_table[nums[i]] = i