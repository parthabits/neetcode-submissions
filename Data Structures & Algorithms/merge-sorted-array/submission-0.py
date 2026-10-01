class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i, j = 0, 0
        nums1_copy.sort()
        nums2.sort()
        current = 0

        while i<m or j<n:
            if i>=m:
                while j<n:
                    nums1[current] = nums2[j]
                    j += 1
                    current += 1
            elif j>=n:
                while i<m:
                    nums1[current] = nums1_copy[i]
                    i += 1
                    current += 1
            elif nums1_copy[i]<nums2[j]:
                nums1[current] = nums1_copy[i]
                i += 1
                current += 1
            else:
                nums1[current] = nums2[j]
                j += 1
                current += 1
