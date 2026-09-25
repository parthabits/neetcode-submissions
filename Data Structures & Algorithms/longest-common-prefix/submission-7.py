class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        first = strs[0]
        minLength = min([len(s) for s in strs])
        current = 0
        while current < minLength:
            for i in range(1, len(strs)):
                if strs[i][current] != first[current]:
                    return lcp
                
            lcp += first[current]
            current += 1
        return lcp


        