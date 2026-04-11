class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if (needed in memory):
                j = memory[needed]
                return [j,i]
            
            memory[nums[i]] = i