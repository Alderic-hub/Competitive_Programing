class Solution(object):
    def escapeGhosts(self, ghosts, target):
        comp = abs(target[0]) + abs(target[1])
        for items in ghosts:
            val = abs(items[0] - target[0]) + abs(items[1] - target[1])
            if val < comp or val == comp:
                return False
        return True
        
