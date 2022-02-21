# 1st solution
# O(n) time | O(h) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    one = dfs(topManager, reportOne)
    two = dfs(topManager, reportTwo)
    idx = 0
    while idx < min(len(one), len(two)):
        if one[idx] == two[idx]:
            idx += 1
        else:
            break
    return one[idx - 1]

def dfs(root, target, path = []):
    if not root:
        return None
    if root.name == target.name:
        return path + [root]
    for node in root.directReports:
        newPath = dfs(node, target, path + [root])
        if newPath:
            return newPath
    return None

# 2nd solution
# O(n) time | O(h) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    level = {topManager: [topManager]}
    isOneFound = False
    isTwoFound = False
    while level:
        if reportOne in level:
            one = level[reportOne]
            isOneFound = True
        if reportTwo in level:
            two = level[reportTwo]
            isTwoFound = True
        if isOneFound and isTwoFound:
            break
        newLevel = {}
        for root in level:
            for node in root.directReports:
                newLevel[node] = level[root] + [node]
        level = newLevel

    for idx in reversed(range(min(len(one), len(two)))):
        if one[idx] == two[idx]:
            return one[idx]

# 3rd solution, official
# O(n) time | O(d) space
# where n is the number of people in the org and d is the depth (height) of the org chart
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
