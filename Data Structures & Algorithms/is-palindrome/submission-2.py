class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)

        l = 0
        r = len(cleaned) - 1

        while l <= r:
            if cleaned[l].lower() != cleaned[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
            