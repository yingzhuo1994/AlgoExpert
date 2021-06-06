def groupAnagrams(words):
    # Write your code here.
	d = {}
	for w in words:
		key = tuple(sorted(w))
		d[key] = d.get(key, []) + [w]
	return list(d.values())
