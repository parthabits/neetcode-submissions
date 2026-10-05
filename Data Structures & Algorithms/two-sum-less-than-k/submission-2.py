class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        currentMax = -1
        while i < j:
            if nums[i]+nums[j] > k:
                j-=1
            elif nums[i]+nums[j] < k:
                currentMax = max(currentMax, nums[i]+nums[j])
                i+=1
            else:
                return currentMax
                    
        return currentMax
        