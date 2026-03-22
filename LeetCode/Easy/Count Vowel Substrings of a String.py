class Solution(object):
    def countVowelSubstrings(self, word):
        length_word = len(word)
        ans = 0
        vowels_set = set('aeiou')
        
        for start in range(length_word):
            substring = set()
            for end in range(start, length_word):
                char = word[end]
                if char in vowels_set:
                    substring.add(char)
                    if len(substring) == 5:
                        ans += 1
                else:
                    break
                    
        return ans
