class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        memory = []
        i, j, k = 0, 0, 0

        for i in range(len(word1) + len(word2)):
            if j < len(word1):
                memory.append(word1[j])
                j += 1
            if k < len(word2):
                memory.append(word2[k])
                k += 1
            
        return ''.join(memory)