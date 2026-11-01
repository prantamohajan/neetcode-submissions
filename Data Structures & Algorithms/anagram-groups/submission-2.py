from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            sorted_s = "". join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values())