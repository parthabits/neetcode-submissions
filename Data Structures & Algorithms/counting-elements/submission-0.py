class Solution:
    def countElements(self, arr: List[int]) -> int:
        st = set()
        for a in arr:
            st.add(a)
        s = 0
        for i in arr:
            if i+1 in st:
                s += 1
        return s
        