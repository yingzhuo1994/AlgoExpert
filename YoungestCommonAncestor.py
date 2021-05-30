# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # 1st solution
    # O(d) time | O(d) space
    one = descendantOne
    two = descendantTwo
    ancestorOfOne = []
    while one:
        ancestorOfOne.append(one)
        one = one.ancestor
    while two:
        if two in ancestorOfOne:
            return two
        two = two.ancestor
	return None
    
    # 2nd solution
    # O(d) time | O(1) space
    depthOne = getDepth(descendantOne, topAncestor)
    depthTwo = getDepth(descendantTwo, topAncestor)
    if depthOne >= depthTwo:
        return backTrack(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backTrack(descendantTwo, descendantOne, depthTwo - depthOne)

def getDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backTrack(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant