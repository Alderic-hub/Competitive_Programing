class Solution(object):
    def nextGreatestLetter(self, letters, target):
        val = target
        ans = letters[0]
        for letter in letters:
            if letter > val:
                ans = letter
                break
        return ans

        
