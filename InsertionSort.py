def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i):
           if array[i] < array[j]:
               array[j], array[j+1:i+1] = array[i], array[j:i]
               break
    return array
