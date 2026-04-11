class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start, end = 0, len(numbers) - 1

        while start < end:
            if target == numbers[end] + numbers[start]:
                return [start + 1, end + 1]

            elif numbers[end] + numbers[start] > target:
                end -= 1
            
            elif numbers[end] + numbers[start] < target:
                start += 1

            