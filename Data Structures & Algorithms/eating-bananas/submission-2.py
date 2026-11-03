class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        minSpeed = sys.maxsize


        while lower <= upper:
            mid = (lower + upper) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / mid)
            
            if t > h:
                lower = mid + 1
            else:
                minSpeed = min(minSpeed, mid)
                upper = mid - 1
        return minSpeed