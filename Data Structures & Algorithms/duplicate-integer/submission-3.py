class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for i in nums:
            if i in memory:
                return True
            memory.add(i)
        return False

        