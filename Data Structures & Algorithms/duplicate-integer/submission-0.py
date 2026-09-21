class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict.keys():
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for k in nums_dict.keys():
            if nums_dict[k] > 1:
                return True
        
        return False
        