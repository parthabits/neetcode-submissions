class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                tmp_res = [0]*(i+1)
                tmp_res[0], tmp_res[-1] = 1, 1
                for j in range(1, i):
                    tmp_res[j] = res[i-1][j-1] + res[i-1][j]
                res.append(tmp_res)
        return res
        