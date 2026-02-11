class Solution(object):
    def restoreString(self, s, indices):
        ans = list()
        soreted_indices = sorted(indices)
        for items in soreted_indices:
            ans.append(s[indices.index(items)])
        ans = ''.join(ans)
        return ans
        
