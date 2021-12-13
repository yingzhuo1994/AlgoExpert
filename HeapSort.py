# 1st solution, max-heap
# O(nlogn) time | O(1) space
def heapSort(array):
    # Write your code here.
    buildHeap(array)
    for i in reversed(range(1, len(array))):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)
    return array


def heapify(array, idx, end):
    left = 2 * idx + 1
    right = 2 * idx + 2
    largest = idx
    if left < end and array[largest] < array[left]:
        largest = left

    if right < end and array[largest] < array[right]:
        largest = right

    if largest != idx:
        array[largest], array[idx] = array[idx], array[largest]
        heapify(array, largest, end)

def buildHeap(array):
    for i in reversed(range(len(array) // 2)):
        heapify(array, i, len(array))