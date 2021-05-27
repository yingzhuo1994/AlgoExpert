# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        level = [self]
        while level:
            curLevel = []
            for node in level:
                array.append(node.name)
                curLevel.extend(node.children)
            level = curLevel
        return array
