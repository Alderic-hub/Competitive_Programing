class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0
        length = len(tickets)
        value = tickets[k]
        sum = 0
        while count < length:
            num = tickets[count]
            if count < k:
                if num < value:
                    sum += num
                else :
                    sum +=value
            elif count > k:
                if num < value:
                    sum +=num
                else:
                    sum += value -1
            count +=1
        sum += value
        return sum 
            


        
