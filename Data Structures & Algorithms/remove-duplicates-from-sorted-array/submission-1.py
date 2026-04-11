class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        read, write = 1, 1
        
        while read < len(nums):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write