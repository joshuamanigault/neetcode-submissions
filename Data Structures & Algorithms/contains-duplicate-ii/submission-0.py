class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in indexes and abs(indexes[num] - i) <= k:
                return True

            indexes[nums[i]] = i
        return False