# 1st solution
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    lst = [ 0 for _ in range(height + 1)]
	lst[0] = 1
	for i in range(1, height + 1):
		for k in range(1, maxSteps + 1):
			if i - k >= 0:
				lst[i] += lst[i -k]
	return lst[-1]
