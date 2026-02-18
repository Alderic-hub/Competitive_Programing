class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        lis = []
        ans = []
        for letter in s:
            if letter in vowel:
                lis.append(letter)
        length = len(lis) -1
        for item in s:
            if item in vowel:
                ans.append(lis[length])
                lis.pop()
                length -=1
            else:
                ans.append(item)
        ans = ''.join(ans)
        return ans
        
        
