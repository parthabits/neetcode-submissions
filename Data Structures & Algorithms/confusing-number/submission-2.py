class Solution:
    def confusingNumber(self, n: int) -> bool:
        cn_dict = {
            0:0, 
            1:1,
            2:"Invalid",
            3:"Invalid",
            4:"Invalid",
            5:"Invalid",
            6:9,
            7:"Invalid",
            8:8,
            9:6
        }
        str_n, str_result = str(n), ""
        for c in str_n:
            int_c = int(c)
            if str(cn_dict[int_c]) == "Invalid":
                return False
            str_result += str(cn_dict[int_c])
        return str_n!=str_result[::-1]
        