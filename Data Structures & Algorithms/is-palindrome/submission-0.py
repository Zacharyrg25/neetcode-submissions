class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(filter(str.isalnum, s)).lower()
        if s_clean == s_clean[::-1]:
            return True
        return False
