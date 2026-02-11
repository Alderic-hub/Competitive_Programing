class Solution(object):
    def queryResults(self, limit, queries):
        answer= []
        balls = dict()
        colors = dict()
        for ball,color in queries:
            if ball not in balls:
                balls[ball] = color
                colors[color] = colors.get(color,0)+1
            else:
                val = balls[ball]
                colors[val] = colors.get(val)-1
                if colors[val] == 0:
                    del colors[val] 
                balls[ball] = color
                colors[color] = colors.get(color,0)+1
            
                            
            answer.append(len(colors))
        return answer

            
