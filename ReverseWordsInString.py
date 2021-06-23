# O(n) time | O(n) space
def reverseWordsInString(string):
    # Write your code here.
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        ch = string[idx]

        if ch == ' ':
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == ' ':
            words.append(' ')
            startOfWord = idx
    
    words.append(string[startOfWord:])

    return ''.join(words[::-1])
