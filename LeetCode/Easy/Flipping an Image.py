class Solution(object):
    def flipAndInvertImage(self, image):
        ans = []
        for items in image:
            items.reverse()
            ans_list = []
            for item in items:
                if item == 0:
                    ans_list.append(1)
                else:
                    ans_list.append(0)
                
            ans.append(ans_list)
        return ans
        
