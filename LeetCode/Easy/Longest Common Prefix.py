    def longestCommonPrefix(self, strs):
        truth = False
        ret = []
        first = list(strs[0])
        length = len(strs)
        if length == 1:
            return strs[0]
        for n in range(1,length):
            ans = []
            for m in range(len(first)):
                if m < len(first) and m < len(strs[n]):
                    if strs[n][m] == first[m]:
                        ans.append(first[m])
                    else:
                        break 
                else:
                    break
            if not truth or len(ans) < len(ret):
                ret[:] = ans 
            truth = True
        return "".join(ret)
