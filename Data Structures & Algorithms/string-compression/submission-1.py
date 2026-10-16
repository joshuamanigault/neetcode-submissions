class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        chars = List[str]
        ["1", "1", "2"]
          w    r
          
        """
        w, r = 0, 0
        n = len(chars)

        while r < n:        
            char = chars[r]
            count = 0
            while r < n and chars[r] == char:
                count += 1
                r += 1
            
            chars[w] = char
            w += 1
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1

        return w