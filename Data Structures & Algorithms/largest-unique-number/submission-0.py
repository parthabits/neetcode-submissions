class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict.keys():
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        nums.sort()
        i = len(nums) - 1
        while i >= 0:
            if nums_dict[nums[i]] == 1:
                return nums[i]
            i -= 1
        return -1
        