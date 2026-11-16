class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        see = set () #khali set nilam 
        for i in nums: # ekta kore i nicchi 
            if i in see: #check korcchi i ache ki na 
                return True # thakle ami true bolchi 
            see.add(i) # na thkle juri vitor e rhklam pore dekar jonoo 
        return False  # na paile false bolbo