class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        leftM, rightM = height[l], height[r]

        # rightM = 3 leftM = 3
        # r = 4, l = 3
        # result = 9

        while l < r:
            if leftM < rightM:
                l += 1
                leftM = max(leftM, height[l])
                result += leftM - height[l]
            else:
                r -= 1
                rightM = max(rightM, height[r])
                result += rightM - height[r]

        return result
        