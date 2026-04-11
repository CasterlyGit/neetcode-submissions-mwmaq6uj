class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memory = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            memory[i] = memory.get(i,0) + 1;

        for i in t:
            if i not in memory:
                return False
            memory[i] = memory.get(i,0) - 1;

            if memory[i] < 0:
                return False
        
        return True