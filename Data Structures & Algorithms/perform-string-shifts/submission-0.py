class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for shft in shift:
            direction, amount = shft[0], shft[1]
            if direction == 0:
                i = 0
                while i < amount:
                    tmp_s = s[1:] + s[0]
                    s = tmp_s
                    i += 1
                #print(s)
            elif direction == 1:
                i = 0
                while i < amount:
                    tmp_s = s[-1] + s[:-1]
                    s = tmp_s
                    i += 1
                    #print(s)
        
        return s
        