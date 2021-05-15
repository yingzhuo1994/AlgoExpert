def firstNonRepeatingCharacter(string):
    # Write your code here.
    # O(n) time | O(1) space
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index=[string.index(l) for l in alphabet if string.count(l) == 1]
    return min(index) if len(index) > 0 else -1
