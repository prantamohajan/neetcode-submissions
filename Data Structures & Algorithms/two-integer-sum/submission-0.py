class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in pre:
                return [pre[diff],i]
            pre[n]=i

        
        