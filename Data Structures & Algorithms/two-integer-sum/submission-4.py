class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in vals:
                return [vals[dif], i]
            vals[nums[i]] = i
