class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict_keyboard = {}
        for i in range(len(keyboard)):
            dict_keyboard[keyboard[i]] = i
        
        s = dict_keyboard[word[0]]
        current = dict_keyboard[word[0]]

        for w in word[1:]:
            s += abs(current - dict_keyboard[w])
            current = dict_keyboard[w]
        return s





        