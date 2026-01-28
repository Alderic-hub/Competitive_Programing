    def isCovered(self, ranges, left, right):
        big_list = []
        for items in ranges:
            for n in range(items[0],items[1]+1):
                big_list.append(n)
        for n in range(left,right+1):
            if n not in big_list:
                return False
        return True
