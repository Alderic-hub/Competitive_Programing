    def isPalindrome(self, x):
        string = str(x)
        length = len(string)-1
        start = 0
        while start < length:
            if string[start] != string[length]:
                return False
            length -= 1
            start += 1
        return True 
