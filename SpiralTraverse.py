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
# O(n) time | O(n) space
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

# O(n) time | O(n) space
# where n is the total number of elements in the array
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        
        for col in reversed(range(startCol, endCol)):
            # Handle the edge case when there's a single row
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this row, which
            # we've already counted in the first for loop above.
            # See Test Case 8 for an example of this edge case.
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        
        for row in reversed(range(startRow + 1, endRow)):
            # Handle the edge case when there's a single column
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this column, which
            # we've readly counted in the second for loop above.
            # See Test Case 9 for an example of this edge case.
            if startCol == endCol:
                break
            result.append(array[row][startCol])
    
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result

# O(n) time | O(n) space
# where n is the total number of elements in the array
def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return 
    
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])
    
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])
    
    for col in reversed(range(startCol, endCol)):
        # Handle the edge case when there's a single row
        # in the middle of the matrix. In this case, we don't
        # want to double-count the values in this row, which
        # we've already counted in the first for loop above.
        # See Test Case 8 for an example of this edge case.
        if startRow == endRow:
            break
        result.append(array[endRow][col])
    
    for row in reversed(range(startRow + 1, endRow)):
        # Handle the edge case when there's a single column
        # in the middle of the matrix. In this case, we don't
        # want to double-count the values in this row, which
        # we've already counted in the second for loop above.
        # See Test Case 9 for an example of this edge case.
        if startCol == endCol:
            break
        result.append(array[row][startCol])
    
    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)