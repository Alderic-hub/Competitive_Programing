class Solution(object):
    def isAnagram(self, s, t):
        s_Dict = {}
        t_Dict = {}
        for letter in s:
            if letter not in s_Dict:
                s_Dict[letter] = s.count(letter)
        for letter in t:
            if letter not in t_Dict:
                t_Dict[letter] = t.count(letter)
        return s_Dict == t_Dict

        
