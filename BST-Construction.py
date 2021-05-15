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


# t = BST(10)
# t.insert(5)
# t.insert(15)
# print(t)
# t.remove(10)

t = BST(10)
t.insert(5)
print(t)
t.remove(10)
print(t)
