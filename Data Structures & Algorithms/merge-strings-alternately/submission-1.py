class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        current = "word1"
        res = ""
        while i < len(word1) or j < len(word2):
            if i >= len(word1):
                res += word2[j:]
                return res
            elif j >= len(word2):
                res += word1[i:]
                return res
            elif current == "word1":
                res += word1[i]
                i += 1
                current = "word2"
            else:
                res += word2[j]
                j += 1
                current = "word1"
        return res
            


        