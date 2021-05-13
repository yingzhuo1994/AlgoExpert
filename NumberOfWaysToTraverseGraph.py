def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    # O(mn) time | O(n) space
    steps = [1 for _ in range(width)]
    for i in range(height - 1):
        for j in reversed(range(width - 1)):
            steps[j] = steps[j] + steps[j + 1]
    return steps[0]

