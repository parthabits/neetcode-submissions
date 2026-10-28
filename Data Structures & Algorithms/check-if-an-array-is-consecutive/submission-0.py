class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[j]-nums[i]==0 or nums[j]-nums[i]>1:
                return False
            i += 1
            j += 1
        return True
