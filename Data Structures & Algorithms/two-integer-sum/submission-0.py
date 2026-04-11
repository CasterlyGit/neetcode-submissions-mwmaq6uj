class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_dict = {}

        for current_index, current_value in enumerate(nums):
            complement = target - current_value

            if complement in complement_dict:
                return [complement_dict[complement], current_index]

            complement_dict[current_value] = current_index