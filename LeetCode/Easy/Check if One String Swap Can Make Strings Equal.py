class Solution(object):
    def areAlmostEqual(self, s1, s2):
        s1 = list(s1)
        s2 = list(s2)
        counter = 0
        swap = []
        for n in range(len(s1)):
            if s1[n] != s2[n]:
                swap.append(n)
                counter += 1
            if counter > 2:
                return False
        if counter == 2:
            s1[swap[0]],  s1[swap[1]]=  s1[swap[1]],  s1[swap[0]]
        if s1 == s2:
            return True 
        return False
