class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_dict = {}
        for st in s:
            if st in s_dict.keys():
                s_dict[st] += 1
            else:
                s_dict[st] = 1
        
        odd_count = 0
        for k, v in s_dict.items():
            if v%2 == 1:
                if odd_count > 0:
                    return False
                odd_count += 1
        return odd_count <= 1
        