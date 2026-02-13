class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img or not img[0]:
            return []
        answer = []
        large_img = []
        row = len(img)
        column = len(img[0])
        large_img.append([None] * (column + 2))
        for items in img:
            large_img.append([None] + items + [None] )
        large_img.append([None] * (column + 2)) 

        for r in range(1,row+1):
            ans_list = []
            for c in range(1,column + 1):
                total = 0
                count = 0
                for val in[                
                    large_img[r][c],       
                    large_img[r][c+1],    
                    large_img[r][c-1],     
                    large_img[r+1][c],     
                    large_img[r+1][c+1],  
                    large_img[r+1][c-1],
                    large_img[r-1][c],    
                    large_img[r-1][c+1],  
                    large_img[r-1][c-1]
                    ]:
                    if val is not None:
                        total += val
                        count +=1

                ans_list.append(total // count)
            answer.append(ans_list)
        return answer

        
