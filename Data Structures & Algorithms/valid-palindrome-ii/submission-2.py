class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(st: str) -> bool:

            i, j = 0, len(st) - 1

            while i < j:
                if not st[i] == st[j]: 
                    return False
                i += 1
                j -= 1
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start] == s[end]:
                return isPalindrome(s[start+1:end+1]) or isPalindrome(s[start:end])
            start += 1
            end -= 1
        return True