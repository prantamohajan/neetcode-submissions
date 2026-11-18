class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        # ১. প্রতিটি সংখ্যা কতবার এসেছে তা গুনে ডিকশনারিতে রাখা
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # ২. ফ্রিকোয়েন্সি অনুযায়ী বাক্স বা লিস্ট তৈরি করা (Bucket Sort)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
            
        # ৩. পেছনের দিক থেকে (বেশি ফ্রিকোয়েন্সি থেকে) K টি সংখ্যা সংগ্রহ করা
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res