class Solution(object):
    def compress(self, chars):
        ans = []
        count = 1
        length = len(chars)-2
        if length == -1:
            return len(chars)
        for n in range(len(chars)-1):
            if chars[n] == chars[n+1]:
                count += 1
            else:
                ans.append(chars[n])
                if count != 1:
                    val = str(count)
                    for items in val:
                        ans.append(items)
                count = 1
            if n == length:
                ans.append(chars[n+1])
                if count != 1:
                    val = str(count)
                    for items in val:
                        ans.append(items)
        for n in range(len(ans)):
            chars[n] = ans[n]
        for _ in range(len(ans),len(chars)):
            chars.pop()
        return len(ans)
