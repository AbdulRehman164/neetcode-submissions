class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        b = [[] for i in range(len(nums))]
        for key in freq:
            b[freq[key] - 1].append(key)
        res = []
        for arr in reversed(b):
            for val in arr:
                res.append(val)
                if len(res) == k:
                    return res
