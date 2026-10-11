class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_freq, s2_freq = Counter(s1), Counter(s2[0:n1])
        if s1_freq == s2_freq:
            return True
        
        l, r = 0, n1
        while r < n2:
            s2_freq[s2[r]] += 1
            s2_freq[s2[l]] -= 1

            if s2_freq == s1_freq:
                return True

            l += 1
            r += 1
        return False

        