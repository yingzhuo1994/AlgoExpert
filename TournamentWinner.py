HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ''
    teams = {currentBestTeam: 0}
    for index, competition in enumerate(competitions):
        a, b = competition
        winningTeam = a if results[index] == HOME_TEAM_WON else b
        updateScores(winningTeam, 3, teams)
        if teams[winningTeam] > teams[currentBestTeam]:
            currentBestTeam = winningTeam
    print(teams)
    return currentBestTeam

def updateScores(team, points, teams):
    if team not in teams:
        teams[team] = 0
    teams[team] += points

def tournamentWinner(competitions, results):
    # Write your code here.
    point = 3
    currentWinner = ''
    teams = {currentWinner: 0}

    for i, competition in enumerate(competitions):
        if results[i] == 1:
            winningTeam = competition[0]
        else:
            winningTeam = competition[1]
        if winningTeam not in teams:
            teams[winningTeam] = point
        else:
            teams[winningTeam] += point
        if teams[winningTeam] > teams[currentWinner]:
            currentWinner = winningTeam
    return currentWinner
