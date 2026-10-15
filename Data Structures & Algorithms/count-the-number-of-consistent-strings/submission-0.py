class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        isCon = True
        for s in words:
            isCon = True

            for i in range(len(s)):
                if s[i] not in allowed:
                    isCon = False
                    break
            
            if isCon:
                count += 1
        return count
                
        