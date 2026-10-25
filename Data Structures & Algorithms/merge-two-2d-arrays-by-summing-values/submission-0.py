class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for arr in nums1:
            id, value = arr[0], arr[1]
            if id in d.keys():
                d[id]+=value
            else:
                d[id]=value
        for arr in nums2:
            id, value = arr[0], arr[1]
            if id in d.keys():
                d[id]+=value
            else:
                d[id]=value
        res = []
        for k, v in d.items():
            res.append([k, v])
        res.sort()
        return res

        
