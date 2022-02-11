# O(n + m) time | O(c) space
# where n is the number of characters, m is the length of the document
# and c is the number of unique characters in the characters string
def generateDocument(characters, document):
    dic = getDic(characters)
    for elem in document:
        if elem in dic and dic[elem] > 0:
            dic[elem] -= 1
        else:
            return False
    return True

def getDic(s):
    dic = {}
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    return dic
