def minNumberOfCoinsForChange(n, denoms):
    # O(nd) time | O(n) space
    lst = [float('inf') for _ in range(n + 1)]
	lst[0] = 0
	denoms.sort()
    for denom in denoms:
        for i in range(len(lst)):
            if denom <= i and lst[i - denom] >= 0:
				lst[i] = min(lst[i], 1 + lst[i - denom])
    return lst[-1] if lst[-1] != float('inf') else - 1

