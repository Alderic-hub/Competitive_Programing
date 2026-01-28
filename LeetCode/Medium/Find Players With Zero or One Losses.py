    def findWinners(self, matches):
        winner_list = []
        losser_list = []
        answer = []
        for items in matches:
            winner_list.append(items[0])
            losser_list.append(items[1])
        ans_win = list(set(winner_list)-set(losser_list))
        counts = {}
        for item in losser_list:
            counts[item] = counts.get(item, 0) + 1
        ans_loss = [item for item, count in counts.items() if count == 1]
        
        ans_win.sort() 
        ans_loss.sort()           
        answer.append(ans_win)
        answer.append(ans_loss)
        return answer
