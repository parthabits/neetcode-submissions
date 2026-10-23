class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        res = [0]*len(nums)
        while j<len(nums):
            if nums[i] == nums[j]:
                nums[i]*=2
                nums[j]=0
            i += 1
            j += 1
        cur = 0
        for n in nums:
            if n > 0:
                res[cur]=n
                cur+=1
        return res