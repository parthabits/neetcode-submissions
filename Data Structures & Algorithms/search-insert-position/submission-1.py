class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        res = len(nums)
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
        