def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    lst = [-1 for _ in range(n + 1)]
	lst[0] = 0
	denoms.sort()
    for denom in denoms:
        for i in range(len(lst)):
            if lst[i] >= 0:
                lst[i] = min(lst[i], 1 + lst[i - denom])
            else:
                lst[i] = 1 + lst[i - denom]
		print(denom, lst)
    return lst[-1]
