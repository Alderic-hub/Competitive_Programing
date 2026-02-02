#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a_pointer = 0
        b_pointer = 0
        b_last = len(b)
        a_last = len(a)
        a = sorted(a)
        b = sorted(b)
        while b_pointer < b_last and a_pointer < a_last:
            val1 = a[a_pointer]
            val2 = b[b_pointer]
            if val1 == val2:
                a_pointer += 1
                b_pointer += 1
            elif val1 < val2:
                a_pointer += 1
            else:
                break
        if b_last == b_pointer:
            return True
        return False
                
                
        
        
    
    
    
    
