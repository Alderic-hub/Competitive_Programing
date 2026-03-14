class Solution(object):
    def dividePlayers(self, skill):
        answer = 0
        ans = []
        start = 0
        end = len(skill)-1
        skill.sort()
        while start < end:
            lis = [skill[start],skill[end]]
            ans.append(lis)
            start += 1
            end -= 1
        comp = sum(ans[0])
        for items in ans:
            val = sum(items)
            if val != comp:
                return -1
            else:
                answer += (items[0]*items[1])
        return answer
        

        
