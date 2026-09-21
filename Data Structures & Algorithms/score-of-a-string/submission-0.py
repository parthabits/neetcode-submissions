class Solution:
    def scoreOfString(self, s: str) -> int:
        score, i, j = 0, 0, 1
        while j < len(s):
            score += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1
        return score
        
        