class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                count = 1
                cur = num
                while (cur + 1) in nums_set:
                    count += 1
                    cur += 1
                res = max(count, res)
        return res
