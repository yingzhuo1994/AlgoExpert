def minNumberOfCoinsForChange(n, denoms):
    # O(nd) time | O(n) space
    lst = [float('inf') for _ in range(n + 1)]
	lst[0] = 0
    for denom in denoms:
        for i in range(len(lst)):
            if denom <= i:
				lst[i] = min(lst[i], 1 + lst[i - denom])
    return lst[-1] if lst[-1] != float('inf') else - 1

