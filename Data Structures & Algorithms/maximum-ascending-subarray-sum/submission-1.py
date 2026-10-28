class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            currentSum = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j]<= nums[j-1]:
                    break
                currentSum += nums[j]
            res = max(res, currentSum)
        return res
        