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