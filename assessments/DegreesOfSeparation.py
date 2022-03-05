# 1st solution
# O(v + e) time | O(v) space
# where v is the number of vertices (people) in the friends graph
# and e is the number of edges (total friends) in the friends graph
def degreesOfSeparation(friendsLists, personOne, personTwo):
    oneCount = bfs(friendsLists, personOne)
    twoCount = bfs(friendsLists, personTwo)
    if oneCount < twoCount:
        return personOne
    elif oneCount > twoCount:
        return personTwo
    else:
        return ""

def bfs(friendsLists, start):
    visited = {start: 0}
    degree = 0
    level = [start]
    while level:
        newLevel = []
        degree += 1
        if degree > 6:
            break
        for name in level:
            for friend in friendsLists[name]:
                if friend in visited:
                    continue
                visited[friend] = degree
                newLevel.append(friend)
        level = newLevel
    count = len(friendsLists) - len(visited)
    return count

# 2nd solution
# O(v + e) time | O(v) space
# where v is the number of vertices (people) in the friends graph
# and e is the number of edges (total friends) in the friends graph
def degreesOfSeparation(friendsLists, personOne, personTwo):
    degreesOne = getDegreesOfSeparation(friendsLists, personOne)
    degreesTwo = getDegreesOfSeparation(friendsLists, personTwo)
    numDegreesOverSixOne = getNumDegreesOverSix(friendsLists, degreesOne)
    numDegreesOverSixTwo = getNumDegreesOverSix(friendsLists, degreesTwo)
    if numDegreesOverSixOne < numDegreesOverSixTwo:
        return personOne
    elif numDegreesOverSixOne > numDegreesOverSixTwo:
        return personTwo
    else:
        return ""

def getDegreesOfSeparation(friendsLists, origin):
    degrees = {}
    visited = {}
    queue = [{"person": origin, "degree": 0}]
    while len(queue) > 0:
        personInfo = queue.pop(0)
        person, degree = personInfo["person"], personInfo["degree"]
        degrees[person] = degree
        for friend in friendsLists[person]:
            if friend in visited:
                continue
            visited[friend] = True
            queue.append({"person": friend, "degree": degree + 1})
    
    for person in friendsLists:
        if person not in visited:
            degrees[person] = float("inf")
    return degrees

def getNumDegreesOverSix(friendsLists, degrees):
    numDegreesOverSix = 0
    for person in friendsLists:
        if degrees[person] > 6:
            numDegreesOverSix += 1
    return numDegreesOverSix