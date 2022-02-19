# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

# 1st solution
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.minHeap = MinHeap([])
        self.maxHeap = MinHeap([])

    # O(log(n)) time | O(n) space
    def insert(self, number):
        minHeap, maxHeap = self.minHeap, self.maxHeap
        maxHeap.insert(-number)
        value = -maxHeap.remove()
        minHeap.insert(value)
        value = minHeap.remove()
        if minHeap.length <= maxHeap.length:
            minHeap.insert(value)
        else:
            maxHeap.insert(-value)

        if minHeap.length == maxHeap.length:
            self.median = (minHeap.peek() - maxHeap.peek()) / 2.0
        else:
            self.median = float(minHeap.peek())

    def getMedian(self):
        return self.median
	
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.length = len(array)

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
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        # Write your code here.
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        self.length -= 1
        return valueToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        self.length += 1

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

# 2nd solution
from heapq import heappush, heappop
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.minHeap =[]
        self.maxHeap = []

    # O(log(n)) time | O(n) space
    def insert(self, number):
        minHeap, maxHeap = self.minHeap, self.maxHeap
        heappush(maxHeap, -number)
        value = -heappop(maxHeap)
        heappush(minHeap, value)
        value = heappop(minHeap)
        if len(minHeap) <= len(maxHeap):
            heappush(minHeap, value)
        else:
            heappush(maxHeap, -value)

        if len(minHeap) == len(maxHeap):
            self.median = (minHeap[0] - maxHeap[0]) / 2.0
        else:
            self.median = float(minHeap[0])

    def getMedian(self):
        return self.median