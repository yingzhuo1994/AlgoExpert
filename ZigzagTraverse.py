# 1st solution
# O(n) time | O(n) space
def zigzagTraverse(array):
    row = len(array) - 1
    col = len(array[0]) - 1
    seq = -1
    num_of_lines = 0
    lst = []
    while num_of_lines <= row + col:
        if seq > 0:
            i, j = num_of_lines, 0
            while j <= col:
                j = num_of_lines - i
                if 0 <= i <= row and 0 <= j <= col:
                    lst.append(array[i][j])
                i -= 1
        else:
            i, j = 0, num_of_lines
            while i <= row:
                i = num_of_lines - j
                if 0 <= i <= row and 0 <= j <= col:
                    lst.append(array[i][j])
                j -= 1
        num_of_lines += 1
        seq *= -1
    return lst

# 2nd solution
# O(n) time | O(n) space
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                # notice the stop condition sequnce
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                # notice the stop condition sequnce
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width