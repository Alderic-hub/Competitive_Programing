class Solution(object):
    def lengthOfLongestSubstring(self, s):
        end = len(s)
        arr= []
        start = 0
        ans = []
        if s == '':
            return 0
        while start < end:
            if s[start] not in arr:
                arr.append(s[start])
            else:
                val = arr.index(s[start])
                arr = arr[val+1:]
                arr.append(s[start])
            start += 1
            ans.append(len(arr))

        answer = max(ans)
        return answer  
