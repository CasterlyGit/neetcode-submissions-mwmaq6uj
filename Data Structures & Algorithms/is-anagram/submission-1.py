class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memory = {}
        for i in s:
            memory[i] = memory.get(i, 0) + 1
            
        for i in t:
            memory[i] = memory.get(i, 0) - 1

        for i in memory.values():
            if i != 0:
                return False
        return True