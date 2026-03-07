class Solution:
    def frequencySort(self, s: str) -> str:
        ans =Counter(s)
        answer = ""
        ans = sorted(ans.items(), key=lambda item: item[1], reverse=True)
        for key,value in ans:
            for j in range(value):
                answer += key
        return answer
                 

        
