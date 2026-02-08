class Solution(object):
    def uniqueMorseRepresentations(self, words):
        moreseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ansMors = []
        ans = []
        for word in words:
            wordMors = ''
            for letter in word:
                wordMors += moreseCode[ord(letter)-97]
            ans.append(wordMors)

        return len(set(ans))



        
