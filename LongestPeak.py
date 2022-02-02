# 1st solution
def longestPeak(array):
	if len(array) < 3:
		return 0
	longest = 0
	i = 1
	while i < len(array) - 1:
		if array[i - 1] < array[i] and array[i] > array[i + 1]:
			peakIndex = i
			k = 1
			while i - k > 0 and array[i - k -1] < array[i - k]:
				k += 1
			left = i - k
			k = 1
			while i + k < len(array) - 1 and array[i + k] > array[i + k + 1]:
				k += 1
			right = i + k
			if right - left + 1 > longest:
				longest = right - left + 1
			i = right + 1
		else:
			i += 1
	return longest

    # 2nd solution
    def peakLength(array, i):
		p1 = i - 1
		p2 = i + 1
		if array[p1] < array[i] and array[i] > array[p2]:
			while p1 >= 0 and array[p1] < array[p1 + 1]:
				p1 -= 1
			while p2 < len(array) and array[p2] < array[p2 - 1]:
				p2 += 1
			return [p1 + 1, p2 - 1]
		else:
			return [i + 1, i]

	if len(array) < 3:
		return 0
	longest = 0
	i = 1
	while i < len(array) - 1:
		p1, p2 = peakLength(array, i)
		if p2 - p1 > longest:
			longest = p2 - p1 + 1
		i = p2 + 1
	return longest
