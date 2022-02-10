# 1st solution
# O(n) time | O(n) space
def runLengthEncoding(string):
    if not string:
        return []
    lst = []
    count = 1
    ch = string[0]
    i = 1
    while i < len(string):
        if string[i] == ch and count < 9:
            count += 1
        else:
            lst.append(str(count))
            lst.append(ch)
            ch = string[i]
            count = 1
        i += 1
    lst.append(str(count))
    lst.append(ch)
    return ''.join(lst)

# 2nd solution
# O(n) time | O(n) space
def runLengthEncoding(string):
    encodedStringCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)
            currentRunLength = 0
        
        currentRunLength += 1
    
    # Handle the last run.
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[-1])

    return "".join(encodedStringCharacters)