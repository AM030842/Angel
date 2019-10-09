def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def newPlayer():
    score1 = float(input("Please input the first round score"))
    score2 = float(input("Please input the second round score"))
    playerName = float(input("Please input the name of the player"))

    totalScore = score1 + score2
    return playerName, totalScore


while True:
    players = []
    players.append(newPlayer())
