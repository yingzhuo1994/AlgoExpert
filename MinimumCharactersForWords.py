# 1st solution
def minimumCharactersForWords(words):
    # Write your code here.
    dic = {}
    for word in words:
        curDic = {}
        for ch in word:
            curDic[ch] = curDic.get(ch, 0) + 1
        for k, v in curDic.items():
            dic[k] = max(dic.get(k, 0), v)
    lst = []
    for k, v in dic.items():
        lst.extend([k] * v)
    return lst

# 2nd solution
# O(n * l) time | O(c) space - where n is the number of words.
# l is the length of the longest word, and c is the number of unique characters across all words.
# See notes under video explanation for details about the space complexity.
def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)
    
    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
    characterFrequencies = {}

    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0
        
        characterFrequencies[character] += 1
    
    return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency

def makeArrayFromCharacterFrequencies(characterFrequencies):
    characters = []

    for character in characterFrequencies:
        frequency = characterFrequencies[character]

        for _ in range(frequency):
            characters.append(character)
    
    return characters
