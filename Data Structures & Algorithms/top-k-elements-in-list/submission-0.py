class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_freq = dict(sorted(freq.items(), reverse=True, key=lambda item: item[1]))
        res = []
        keys = list(sorted_freq.keys())
        for i in range(k):
            res.append(keys[i])
        return res
