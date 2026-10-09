class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        result = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            highest_freq = max(freq.values())

            while (r - l + 1) - highest_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
            


            

        