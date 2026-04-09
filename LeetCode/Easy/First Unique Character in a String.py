class Solution(object):
    def firstUniqChar(self, s):
        string = s
        length = len(string)
        count = 0
        value = False
        while count < length:
            elm = string[count]
            val = string.count(elm)
            if val == 1:
                value = True
                break
            else:
                string = string.replace(elm,'')
                length = len(string)
                count-=1
            count +=1

        if value:
            return s.index(elm)
        return -1
        
