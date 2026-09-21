class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = words
        columns = []
        len_of_words = len(words[0])
        for i in range(len_of_words):
            col = ""
            for word in words:
                if i >= len(word):
                    break
                col += word[i]
            columns.append(col)
        
        for i in range(len(words)):
            if words[i]!= columns[i]:
                return False
        
        return True


        