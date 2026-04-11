class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j+= 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                    
                elif total > 0:
                    k -= 1
                    
                elif total < 0:
                    j += 1
                
        return output