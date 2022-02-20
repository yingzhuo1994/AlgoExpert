# 1st solution
# O(w * n * log(n) + n * w * log(w)) time | O(wn) space
# where w is the number of words and n is the length of the longest word
def groupAnagrams(words):
	if len(words) == 0:
		return []
	
	sortedWords = ["".join(sorted(w)) for w in words]
	indices = [i for i in range(len(words))]
	indices.sort(key = lambda x: sortedWords[x])

	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indices[0]]
	for index in indices:
		word = words[index]
		sortedWord = sortedWords[index]

		if sortedWord == currentAnagram:
			currentAnagramGroup.append(word)
			continue

		result.append(currentAnagramGroup)
		currentAnagramGroup = [word]
		currentAnagram = sortedWord
	
	result.append(currentAnagramGroup)

	return result


# 2nd solution
# O(w * n * log(n)) time | O(wn) space
# where w is the number of words and n is the length of the longest word
def groupAnagrams(words):
    # Write your code here.
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord not in anagrams:
			anagrams[sortedWord] = []
		anagrams[sortedWord].append(word)
	return list(anagrams.values())
