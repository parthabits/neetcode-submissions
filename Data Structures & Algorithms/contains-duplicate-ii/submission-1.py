class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for ke, v in d.items():
            if len(v)<2:
                continue
            elif len(v)==2:
                if abs(v[0]-v[1])<=k:
                    return True
            elif len(v)>2:
                m, n = 0, 1
                while n<len(v):
                    if abs(v[n]-v[m])<=k:
                        return True
                    m += 1
                    n += 1
        return False        