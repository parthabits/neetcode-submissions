class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        a = []
        for i in range(len(arr)):
            if arr[i] in d.keys():
                d[arr[i]][0]+=1
            else:
                d[arr[i]]=[1, i+1]
        print(d)
        for ke, v in sorted(d.items(), key=lambda item: item[1]):
            if v[0] == 1:
                a.append(ke)
        if len(a)>=k:
            return a[k-1]
        return ""
        