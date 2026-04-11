class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        result = nums[n-k:n]
        for i in range(n):
            result.append(nums[i])
            nums[i] = result[i]

    