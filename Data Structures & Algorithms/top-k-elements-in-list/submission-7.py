class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)


        bucket = [[] for _ in range(len(nums)+ 1)]
        for num,freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res