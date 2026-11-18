from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # একটি ডিকশনারি যার ডিফল্ট ভ্যালু হলো লিস্ট []
        ans = defaultdict(list)

        for s in strs:
            # প্রতিটি শব্দকে অক্ষর অনুযায়ী সাজিয়ে একটি 'কী' (Key) বানানো
            sortedS = "".join(sorted(s))
            
            # ওই 'কী'-এর আন্ডারে আসল শব্দটি যুক্ত করে দেওয়া
            ans[sortedS].append(s)

        # ডিকশনারির ভেতরের গ্রুপ বা ভ্যালুগুলো রিটার্ন করা
        return list(ans.values())