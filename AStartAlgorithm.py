# 1st solution
# O(w * h * log(w * h)) time | O(w * h) space
# where w is the width of the graph and h is the height
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)

    nodesToVisit = MinHeap([startNode])

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()

        if currentMinDistanceNode == endNode:
            break

        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue

            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1

            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue

            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(
                neighbor, endNode
            )

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    
    return reconstructPath(endNode)


def initializeNodes(graph):
    nodes = []

    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    
    return nodes

def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col

    return abs(currentRow - endRow) + abs(currentCol - endCol)

def getNeighboringNodes(node, nodes):
    neighbors = []

    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRows - 1: # DOWN
        neighbors.append(nodes[row + 1][col])
    
    if row > 0: # UP
        neighbors.append(nodes[row - 1][col])
    
    if col < numCols - 1: # RIGHT
        neighbors.append(nodes[row][col + 1])
    
    if col > 0:
        neighbors.append(nodes[row][col - 1])
    
    return neighbors

def reconstructPath(endNode):
    if not endNode.cameFrom:
        return []
    
    currentNode = endNode
    path = []

    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom
    
    return path[::-1]

class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distanceFromStart = float("inf") # g
        self.estimatedDistanceToEnd = float("inf") # f = g + h
        self.cameFrom = None

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}

    def isEmpty(self):
        return len(self.heap) == 0
    
    # O(n) time | O(1) space
    def buildHeap(self, array):
        # Write your code here.
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space    
    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        # Write your code here.
        self.heap.append(node)
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].id] = j
        self.nodePositionsInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]
    
    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap
    
    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)


# 2nd solution
# O(w * h * log(w * h)) time | O(w * h) space
# where w is the width of the graph and h is the height
import heapq
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes =  {}
    nodes[(startRow, startCol)] = [getManhattanDistance(startRow, startCol, endRow, endCol), 0]
    stack = [[nodes[(startRow, startCol)][0], (startRow, startCol)]]
    while stack:
        totalDistance, node = heapq.heappop(stack)
        if node == (endRow, endCol):
            break
        neighbors = getNeighbors(graph, node[0], node[1])
        for neighbor in neighbors:
            step = nodes[node][1] + 1
            newDistance = step + getManhattanDistance(neighbor[0], neighbor[1], endRow, endCol)
            if (neighbor in nodes and newDistance < nodes[neighbor][0]) or neighbor not in nodes:
                nodes[neighbor] = [newDistance, step]
                heapq.heappush(stack, [newDistance, neighbor])
    
    return reconstructPath(startRow, startCol, endRow, endCol, graph, nodes)

def getManhattanDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def getNeighbors(graph, row, col):
    neighbors = []
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        newRow = row + dx
        newCol = col + dy
        if 0 <= newRow < len(graph) and 0 <= newCol < len(graph[0]):
            if graph[newRow][newCol] != 1:
                neighbors.append((newRow, newCol))
    return neighbors

def reconstructPath(startRow, startCol, endRow, endCol, graph, nodes):
    path = []
    x, y = endRow, endCol
    if (x, y) not in nodes:
        return []
    while [x, y] != [startRow, startCol]:
        path.append([x, y])
        step = nodes[(x, y)][1]
        neighbors = getNeighbors(graph, x, y)
        for neighbor in neighbors:
            if neighbor in nodes and nodes[neighbor][1] == step - 1:
                x, y = neighbor
                break
    path.append([x, y])
    path.reverse()
    return path