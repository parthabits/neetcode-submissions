class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing, isDecreasing = False, False
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] > nums[i-1]:
                if isDecreasing:
                    return False
                elif not isIncreasing:
                    isIncreasing = True
            elif nums[i] < nums[i-1]:
                if isIncreasing:
                    return False
                elif not isDecreasing:
                    isDecreasing = True
        return True
        