class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = defaultdict(int)
        output = []
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for i in nums:
            memory[i] += 1

        for num, freq in memory.items():
            bucket[freq].append(num)

        for i in range((len(bucket) - 1), 0 , -1):
            for num in bucket[i]:
                output.append(num)
                if k == len(output):
                    return output
        return output



        




