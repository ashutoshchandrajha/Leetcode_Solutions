class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = "qwertyuiop"
        row_2 = "asdfghjkl"
        row_3 = "zxcvbnm"
        final = []
        for word in words:
            r1 = False
            r2 = False
            r3 = False
            for char in word:
                if char in row_1:
                    r1 = True
                if char in row_2:
                    r2 = True
                if char in row_3:
                    r3 = True
            if r1 ^ r2 ^ r3 == True and r1&r2&r3!=True:
                final.append(word)
        return final
