def spiralTraverse(array):
    # Write your code here.
    lst = []
    return recursiveSpiral(array, lst, 0, 0)

def recursiveSpiral(array, lst, row, column):
    if not array:
        return lst
    elif row == 0 and column == 0:
        print('case0', row, column)
        line = array.pop(0)
        lst.extend(line)
        recursiveSpiral(array, lst, 0, -1)
    elif row == 0 and column == -1:
        print('case1', row, column)
        for line in array:
            num = line.pop()
            lst.append(num)
        recursiveSpiral(array, lst, -1, -1)
    elif row == -1 and column == -1:
        print('case2', row, column)
        line = array.pop(-1)
        for i in reversed(range(len(line))):
            lst.append(line[i])
        recursiveSpiral(array, lst, -1, 0)
    elif row == -1 and column == 0:
        print('case3', row, column)
        for i in reversed(range(len(array))):
            num = array[i].pop(0)
            lst.append(num)
        recursiveSpiral(array, lst, 0, 0)

### Joey Iteration solution
def spiralTraverse(array):
    # Write your code here.
    n = len(array)
    m = len(array[0])
    startRow = 0
    endRow = n - 1
    startColumn = 0
    endColumn =  m - 1
    i, j = 0, 0
    lst = []
    while startRow <= endRow and startColumn <= endColumn:
        if i == 0 and j == 0:
            for p in range(startColumn, endColumn + 1):
                lst.append(array[startRow][p])
            startRow += 1
            j = -1
        elif i == 0 and j == -1:
            for p in range(startRow, endRow + 1):
                lst.append(array[p][endColumn])
            endColumn -= 1
            i = -1
        elif i == -1 and j == -1:
            for p in reversed(range(startColumn, endColumn + 1)):
                lst.append(array[endRow][p])
            endRow -= 1
            j = 0
        elif i == -1 and j == 0:
            for p in reversed(range(startRow, endRow + 1)):
                lst.append(array[p][startColumn])
            startColumn += 1
            i = 0
    return lst
