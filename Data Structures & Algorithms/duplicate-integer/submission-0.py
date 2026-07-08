class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        see = set()
        
        for i in nums:
            if i in see:
                return True
            see.add(i)
        return False