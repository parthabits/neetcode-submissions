class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        st = []
        for p in s:
            if p in [')', '}', ']']:
                if len(st) == 0:
                    return False
                tmp = st.pop()
                if tmp!=d[p]:
                    return False
            elif p in ['(', '{', '[']:
                st.append(p)
        return len(st)==0