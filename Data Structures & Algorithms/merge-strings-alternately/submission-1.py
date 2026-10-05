class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        result = []

        for i in range(max(m, n)):
            if i < n:
                result.append(word1[i])
            if i < m:
                result.append(word2[i])
        
        return "".join(result)