class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        start = 0
        end = len(trainers)
        ans = 0
        for player in players:
            if start == end:
                break
            while start < end:
                if trainers[start] >= player:
                    ans += 1
                    start += 1
                    break
                start += 1
        return ans

        
