class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for n in range (len(s)):
            count[s[n]] = count.get(s[n],0)+1
            count[t[n]] = count.get(t[n],0)-1

        for val in count.values():
            if val != 0:
                return False
        return True


