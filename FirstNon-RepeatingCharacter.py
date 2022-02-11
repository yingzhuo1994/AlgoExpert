# 1st solution
# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index=[string.index(l) for l in alphabet if string.count(l) == 1]
    return min(index) if len(index) > 0 else -1

# 2nd solution
# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    
    return -1