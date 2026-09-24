class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_num = {}
        for i in range(len(nums)):
            if nums[i] in d_num.keys():
                d_num[nums[i]].append(i)
            else:
                d_num[nums[i]] = [i]
        
        for i in range(len(nums)):
            if target-nums[i] in d_num.keys():
                ixs = d_num[target-nums[i]]
                if target-nums[i]!=nums[i]:
                    return [i, d_num[target-nums[i]][0]]
                else:
                    for ix in ixs:
                        if ix!=i:
                            return [i, ix]
        return [-1, -1]

        