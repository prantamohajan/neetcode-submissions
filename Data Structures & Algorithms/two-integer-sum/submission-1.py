class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}

        for i , p in enumerate(nums):
            diff = target - p
            if diff in pre:
                return [pre[diff],i]
            pre[p]=i

        
        