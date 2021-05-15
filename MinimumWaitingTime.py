def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	cur, total = 0, 0
	for q in queries:
		total += cur
		cur += q
	return total
