
class Player:
    def init(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns, tvnoOfWickets):
         self.playerName = playerName
         self.playerCountry = playerCountry
         self.playerAge = playerAge
         self.noOfMatches = noOfMatches
         self.noOfRuns = noOfRuns
         self.noOfWickets = noOfWickets

class Team:
    def getMinRuns(self,playerObjects):
        min_runs = min([x.noOfRuns for x in playerObjects])
        for player in playerObjects:
           if player.noOfRuns == min_runs:
                return player
    def getMaxWickets(self,playerObjects):
        max_wik = max([x.noOfWickets for x in playerObjects])
        for player in playerObjects:
            if player.noOfWickets == max_wik:
            1    return player
    
if name=='_main_':
    n = int(input())
    pass_list = []
    for _ in range(n):
        playerName=input()
        playerCountry=input()
        playerAge=int(input())
        noOfMatches=int(input())
        noOfRuns=int(input())
        noOfWickets=int(input())
        obj = Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets)
        pass_list.append(obj)

    org = Team()
    op1 = org.getMinRuns(pass_list)
    op2 = org.getMaxWickets(pass_list)
    print(op1.playerName)
    print(op1.noOfRuns)
    print(op1.playerCountry)
    print(op2.playerName)
    print(op1.noOfWickets)
    print(op1.playerCountry)

