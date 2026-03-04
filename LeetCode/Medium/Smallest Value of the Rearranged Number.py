class Solution(object):
    def smallestNumber(self, num):
        val = list(str(num))
        if num == 0:
            return 0
        if num < 0:
            val.pop(0)
            for n in range(len(val)-1,0,-1):
                for y in range(0,n):
                    if val[y]< val[y+1]:
                        val[y], val[y+1] = val[y+1], val[y]
            val.insert(0,'-')
        else:
            for n in range(len(val)-1,0,-1):
                for y in range(0,n):
                    if val[y]> val[y+1]:
                        val[y], val[y+1] = val[y+1], val[y]
            if val[0] == '0':
                n = 1
                while  n < len(val)-1 and val[n] == '0':
                    n+=1
                val[n], val[0] = val[0], val[n]

            
        return int("".join(val) )
        

        
