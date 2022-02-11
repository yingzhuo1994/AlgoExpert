# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        p = self
        while p:
            if value < p.value:
                if p.left is None:
                    p.left = BST(value)
                    break
                p = p.left
            else:
                if p.right is None:
                    p.right = BST(value)
                    break
                p = p.right
        return self

    def contains(self, value):
        # Write your code here.
        if self.findNode(value) is None:
            return False
        else:
            return True

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        test = self.findNode(value)
        # print(test)
        if test is not None:
            # print(test)
            parentNode, goalNode = test[0], test[1]
            # print(parentNode, goalNode)
            if parentNode is None:
                if goalNode.left is not None and goalNode.right is None:
                    # print(self)
                    # print(goalNode)
                    self.value = self.left.value
                    # Pay attention to the sequence
                    self.right = self.left.right
                    self.left = self.left.left
                    # print(self.left)
                elif goalNode.left is None and goalNode.right is not None:
                    # print('test')
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                elif goalNode.left is not None and goalNode.right is not None:
                    # print('test')
                    # print(self)
                    self.value = self.right.findSmallest(self)
            else:
                if goalNode.left is not None and goalNode.right is None:
                    if goalNode == parentNode.left:
                        parentNode.left = goalNode.left
                    else:
                        parentNode.right = goalNode.left
                elif goalNode.left is None and goalNode.right is not None:
                    if goalNode == parentNode.left:
                        parentNode.left = goalNode.right
                    else:
                        parentNode.right = goalNode.right
                elif goalNode.left is not None and goalNode.right is not None:
                    goalNode.value = goalNode.right.findSmallest(goalNode)
                else:
                    if goalNode == parentNode.left:
                        parentNode.left = None
                    else:
                        parentNode.right = None
        return self

    def findSmallest(self, parentNode, k = 0):
        # print(self)
        p = self
        while p.left:
            k += 1
            parentNode = p
            p = p.left
        value = p.value
        if p.right is None:
            if k != 0:
                parentNode.left = None
            else:
                parentNode.right = None
        else:
            if k != 0:
                parentNode.left = p.right
            else:
                parentNode.right = p.right

        return value

    def findNode(self, value):
        # Write your code here.
        p = self
        parentNode = None
        while p is not None:
            if value < p.value:
                parentNode = p
                p = p.left
            elif value > p.value:
                parentNode = p
                p = p.right
            else:
                return [parentNode, p]
        return None

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            if t.right:
                tree_str += print_tree(t.right, indent + 1)
            if t.left:
                tree_str += print_tree(t.left, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


# 2nd solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # This is a single-node tree; do nothing.
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()

# 3rd solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # This is a single-node tree; do nothing.
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
    
    # simplified
    # def remove(self, value, parentNode=None):
    #     currentNode = self
    #     while currentNode is not None:
    #         if value < currentNode.value:
    #             parentNode = currentNode
    #             currentNode = currentNode.left
    #         elif value > currentNode.value:
    #             parentNode = currentNode
    #             currentNode = currentNode.right
    #         else:
    #             if currentNode.right is not None:
    #                 minValue = currentNode.right.getMinValue()
    #                 currentNode.value = minValue
    #                 currentNode.right.remove(minValue, currentNode)
    #             elif currentNode.left is not None:
    #                 leftValue = currentNode.left.value
    #                 currentNode.value = leftValue
    #                 currentNode.left.remove(leftValue, currentNode)
    #             else:
    #                 if parentNode is not None:
    #                     if parentNode.left == currentNode:
    #                         parentNode.left = currentNode.left
    #                     else:
    #                         parentNode.right = currentNode.left
    #             break
        
    #     return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value