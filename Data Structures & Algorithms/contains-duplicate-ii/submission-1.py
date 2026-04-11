class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        memory = {}

        for i, a in enumerate(nums):

            if a in memory:
                j = memory[a]
                if abs(i - j) <= k:
                    return True

            memory[a] = i
        return False

