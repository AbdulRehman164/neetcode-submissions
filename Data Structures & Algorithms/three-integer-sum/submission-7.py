class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = nums[L] + nums[R] + nums[i]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    res.append([nums[L], nums[R], nums[i]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return res

