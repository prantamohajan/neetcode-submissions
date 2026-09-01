class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for see in nums:
            if see in arr:
                return True
            arr.add(see)
        return False