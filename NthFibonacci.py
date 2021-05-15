def getNthFib(n):
    # Write your code here.
    if n == 1:
		return 0
	if n == 2:
		return 1
	f1, f2 = 0, 1
	k = 3
	while k <= n:
		f1, f2 = f2, f1 + f2
		k += 1
	return f2
