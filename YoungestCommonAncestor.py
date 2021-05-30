# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # 1st solution
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
    