class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start, end = 0, len(numbers) - 1
        output = []

        while start < end:
            if target == numbers[end] + numbers[start]:
                output.append(start + 1)
                output.append(end + 1)
                return output

            elif numbers[end] + numbers[start] > target:
                end -= 1
            
            elif numbers[end] + numbers[start] < target:
                start += 1

        output.append(start + 1)
        output.append(end + 1)
        return output
            