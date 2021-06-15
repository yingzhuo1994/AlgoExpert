# 1st solution
# O(kn) time | O(n) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    lst = [ 0 for _ in range(height + 1)]
	lst[0] = 1
	for i in range(1, height + 1):
		for k in range(1, maxSteps + 1):
			if i - k >= 0:
				lst[i] += lst[i -k]
	return lst[-1]

# 2nd solution
# O(n) time | O(n) space
def staircaseTraversal(height, maxSteps):
	currentNumberOfWays = 0
	waysToTop = [1]

	for currentHeight in range(1, height + 1):
		startOfWindow = currentHeight - maxSteps - 1
		endOfWindow = currentHeight - 1
		if startOfWindow >= 0:
			currentNumberOfWays -= waysToTop[startOfWindow]
		
		currentNumberOfWays += waysToTop[endOfWindow]
		waysToTop.append(currentNumberOfWays)
	
	return waysToTop[height]