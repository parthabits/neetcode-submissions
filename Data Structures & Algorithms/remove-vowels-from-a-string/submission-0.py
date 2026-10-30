class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        for st in s:
            if st in "aeiou":
                continue
            res+=st
        return res
