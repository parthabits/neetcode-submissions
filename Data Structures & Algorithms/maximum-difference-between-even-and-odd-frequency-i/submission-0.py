class Solution:
    def maxDifference(self, s: str) -> int:
        d_s = {}
        for c in s:
            if c in d_s.keys():
                d_s[c] += 1
            else:
                d_s[c] = 1
        odds, evens = [], []
        for k, v in d_s.items():
            if v%2 == 1:
                odds.append(v)
            else:
                evens.append(v)
        odds.sort()
        evens.sort()
        return odds[-1]-evens[0]

        