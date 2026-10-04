class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        res = [-1]*len(nums)
        current = len(res) - 1
        while i <= j:
            if abs(nums[i])>abs(nums[j]):
                res[current] = nums[i]**2
                i += 1
            else:
                res[current] = nums[j]**2
                j -= 1
            current -= 1
        return res

        