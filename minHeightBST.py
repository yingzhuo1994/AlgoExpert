def minHeightBst(array):
    if not array:
        return None
    mid = len(array) // 2
    head = BST(array[mid])
    head.left = minHeightBst(array[:mid])
    head.right = minHeightBst(array[mid+1:])
    return head


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
