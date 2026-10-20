class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """

        - Brute force solution
        - Check every possible subarray
        - Determines if the subarray is equal to K
        - Time complexity: O(N^2)
        - Can we reduce this time complexity?

        """

        # result = 0
        # n = len(nums)

        # for i in range(n):
        #     total = nums[i]
        #     if total == k:
        #         result += 1
        #     for j in range(i + 1, n):
        #         total += nums[j]
        #         if total == k:
        #             result +=1
        
        # return result


        """
        keep track of the counts of prefix sums
        [2, -1, 1, 2] k = 2
        {0: 1}

        sum = 0 + 2 = 2
        diff = 2 - 2 = 0
        result = 0 + 1 = 1

        {0: 1, 2: 1}
        
        sum = 2 + (-1) = 1
        diff = 1 - 2 = -1
        result = 1

        {0: 1, 2: 1, 1: 1}

        sum = 1 + 1 = 2
        diff = 2 - 2 = 0
        result = 2

        {0: 1, 2: 2, 1: 1}

        sum = 2 + 2 = 4
        diff = 4 - 2 = 2
        result = 4

        return 4
        """

        running_sum = 0
        result = 0
        prefix_map = {0: 1}

        for num in nums:
            running_sum += num
            diff = running_sum - k
            if diff in prefix_map:
                result += prefix_map[diff]

            prefix_map[running_sum] = prefix_map.get(running_sum, 0) + 1


        return result
        