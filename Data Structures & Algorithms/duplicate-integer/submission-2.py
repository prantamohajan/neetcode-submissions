class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for bubu in nums:
            if bubu in arr:
                return True
            arr.add(bubu)
        return False