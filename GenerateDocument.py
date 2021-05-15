def generateDocument(characters, document):
    # Write your code here.
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
