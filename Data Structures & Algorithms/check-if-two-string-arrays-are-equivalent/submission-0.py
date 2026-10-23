class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s_word1, s_word2 = "", ""
        for w in word1:
            s_word1+=w
        for w in word2:
            s_word2+=w
        return s_word1 == s_word2
