class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_seqs = []
        for num in nums_set:
            if num - 1 not in nums_set:
                start_seqs.append(num)
        res = 0
        for start in start_seqs:
            count = 1
            while start + count in nums_set:
                count += 1
            res = max(count, res)
        return res
