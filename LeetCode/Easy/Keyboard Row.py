class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans =[]
        for word in words:
            val = word
            word =set(word.lower())
            if word.issubset(row1) or word.issubset(row2) or word.issubset(row3):
                ans.append(val)
        return ans

        
