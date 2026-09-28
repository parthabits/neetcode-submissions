class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        d_nums2 = {}

        for k in range(len(nums2)):
            d_nums2[nums2[k]] = k

        for i in range(len(nums1)):
            ix = d_nums2[nums1[i]]
            for j in range(len(nums2)):
                if nums2[j] > nums1[i] and j>ix:
                    res[i] = nums2[j]
                    break
        return res

        