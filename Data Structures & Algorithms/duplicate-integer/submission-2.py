class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        prevMem = set() 

        for n in nums:
            if n in prevMem:
                return True
            prevMem.add(n)
        return False