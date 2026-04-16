class Solution(object):
    def kthGrammar(self, n, k):
        def helper(current, current_k):
            if current == 1:
                return 0
            half  = current//2
            if current_k > half:
                return 1 - helper(current//2,current_k-half)
            elif current_k <= half:
                return helper(current//2,current_k)
        return helper(2**(n-1),k)

