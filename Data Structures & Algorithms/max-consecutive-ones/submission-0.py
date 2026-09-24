class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c_s, m_s = 0, 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 1:
                    c_s = 1
            else:
                if nums[i] == 0:
                    m_s = max(c_s, m_s)
                    c_s = 0
                else:
                    c_s += 1
        return max(c_s, m_s)
        