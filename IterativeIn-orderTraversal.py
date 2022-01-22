# 1st solution
# O(n) time | O(h) space
def iterativeInOrderTraversal(tree, callback):
    stack = []
    cur = tree
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        callback(cur)
        cur = cur.right
