class Solution(object):
    def getRow(self, rowIndex):
        answer = [[1]]
        count = 1
        while count <= rowIndex:
            subans = []
            subans.append(1)
            leng = len(answer)
            if leng > 1:
                List = answer[leng-1]
                counter = 0
                while counter < leng-1:
                    sum = List[counter] + List[counter + 1]
                    subans.append(sum)
                    counter +=1
            subans.append(1)
            answer.append(subans)
            count +=1
            
        return answer[-1]
        
