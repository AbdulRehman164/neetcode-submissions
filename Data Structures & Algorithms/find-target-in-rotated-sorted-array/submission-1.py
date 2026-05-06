class Solution:
    def binarySearch(self, s, e, nums, target):
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        pivot = -1
        while L <= R:
            mid = (L + R) // 2
            if nums[L] < nums[mid]:
                L = mid
            elif nums[R] > nums[mid]:
                R = mid
            else:
                pivot = mid
                break
        firstHalf = self.binarySearch(0, pivot, nums, target)
        if firstHalf != -1:
            return firstHalf
        else:
            return self.binarySearch(pivot + 1, len(nums) - 1, nums, target)
