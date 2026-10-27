class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {
            0: 1
        }
        running_sum = 0
        result = 0

        for num in nums:
            running_sum += num
            diff = running_sum - k
            if diff in prefix_map:
                result += prefix_map[diff]

            prefix_map[running_sum] = prefix_map.get(running_sum, 0) + 1


        return result
        