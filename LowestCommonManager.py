# 1st solution
# O(n) time | O(h) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    one = binarySearch(topManager, reportOne)
    two = binarySearch(topManager, reportTwo)
    idx = 0
    while idx < min(len(one), len(two)):
        if one[idx] == two[idx]:
            idx += 1
        else:
            break
    return one[idx - 1]

def binarySearch(root, target, path = []):
    if not root:
        return None
    if root.name == target.name:
        return path + [root]
    for node in root.directReports:
        newPath = binarySearch(node, target, path + [root])
        if newPath:
            return newPath
    return None

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
