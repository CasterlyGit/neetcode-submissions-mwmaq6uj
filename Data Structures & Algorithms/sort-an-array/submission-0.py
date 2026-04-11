class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        OFFSET = 50000
        MAX_VAL = 100001

        count = [0] * MAX_VAL
                
        for num in nums:
            count[num + OFFSET] += 1

        result = []
        for i in range(MAX_VAL):
            result.extend([i - OFFSET] * count[i])
        
        return result