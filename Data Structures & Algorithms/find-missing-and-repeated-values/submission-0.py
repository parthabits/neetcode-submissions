class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        tmp, res = [], []
        d = {}
        for gr in grid:
            for g in gr:
                tmp.append(g)
        for t in tmp:
            if t in d.keys():
                d[t]+=1
            else:
                d[t]=1
        for i in d.keys():
            if d[i]>1:
                res.append(i)
        for j in range(1, len(tmp)+1):
            if j not in d.keys():
                res.append(j)
        return res
        