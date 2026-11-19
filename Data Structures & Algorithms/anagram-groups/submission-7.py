from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))

            ans[sortedS].append(s)
        return list(ans.values())
            
        