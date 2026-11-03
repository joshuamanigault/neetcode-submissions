class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged = [item for arr in matrix for item in arr]
        l, r = 0, len(merged) - 1

        while l <= r:
            mid = (l + r) // 2
            if merged[mid] == target:
                return True
            elif merged[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

        