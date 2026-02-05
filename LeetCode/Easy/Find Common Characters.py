class Solution(object):
    def commonChars(self, words):
        base = words[0]
        ans = []
        for letter in base:
            inThere = True
            for n in range(1, len(words)):
                if letter in ans and words[n].count(letter) <= ans.count(letter) or letter not in words[n]:
                    inThere = False
                    break
                    
            if inThere:
                ans.append(letter)
        return ans
                


                    
        
