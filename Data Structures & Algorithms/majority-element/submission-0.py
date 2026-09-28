class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d_nums = {}
        for num in nums:
            if num in d_nums.keys():
                d_nums[num] += 1
            else:
                d_nums[num] = 1
        m_t = len(nums) // 2
        for k, v in d_nums.items():
            if v > m_t:
                return k
        return -1
        