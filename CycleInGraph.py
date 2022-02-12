# 1st solution
# O(v + e) time | O(v) space
# where v is the number of vertices and e is the nmber of edges in the graph
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True
    
    return False

def isNodeInCycle(node, edges, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
            if containsCycle:
                return True
        elif currentlyInStack[neighbor]:
            return True

    currentlyInStack[node] = False
    return False

# 2nd solution
# O(v + e) time | O(v) space
# where v is the number of vertices and e is the nmber of edges in the graph
WHITE, GREY, BLACK = 0, 1, 2
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    colors = [WHITE for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if colors[node] != WHITE:
            continue

        containsCycle = traverseAndColorNodes(node, edges, colors)
        if containsCycle:
            return True
    
    return False

def traverseAndColorNodes(node, edges, colors):
    colors[node] = GREY

    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        if neighborColor == GREY:
            return True
        
        if neighborColor == BLACK:
            continue

        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containsCycle:
            return True
    
    colors[node] = BLACK
    return False