class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dict={}
        res = [0]*len(nums1)
        for i in range(len(nums2)):
            nums2_dict[nums2[i]] = i
        for i in range(len(nums1)):
            res[i] = nums2_dict[nums1[i]]
        return res
        