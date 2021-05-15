def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if n == 0:
        return 1
    elif n < 0:
        return 0
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for value in denoms:
        for i in range(1, n + 1):
            if value <= i:
                results[i] += results[i - value]
    return results[n]
