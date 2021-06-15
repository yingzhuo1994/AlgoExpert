# 1st solution
# O(n + m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] == target:
			return [row, col]
		elif matrix[row][col] > target:
			col -= 1
		else:
			row += 1
	return [-1, -1]

