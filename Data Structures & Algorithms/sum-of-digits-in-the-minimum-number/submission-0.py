class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        m = min(nums)
        s = 0
        for st in str(m):
            s += int(st)
        if s%2 == 0:
            return 1
        else:
            return 0
