# 1st recursive solution
def levenshteinDistance(str1, str2):
    if str1 == str2:
        return 0
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    if str1[0] == str2[0]:
        return levenshteinDistance(str1[1:], str2[1:])
    insertOpt = 1 + levenshteinDistance(str1, str2[1:])
    deletionOpt = 1 + levenshteinDistance(str1[1:], str2)
    substitutionOpt = 1 + levenshteinDistance(str1[1:], str2[1:])
    print(insertOpt, deletionOpt, substitutionOpt)
    return min(insertOpt, deletionOpt, substitutionOpt)

# 2nd dynamic solution
# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    edits = [[j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        edits[i][0] = i
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = min(edits[i-1][j], edits[i][j-1], edits[i-1][j-1]) + 1
    return edits[-1][-1]

# 3rd solution
# O(nm) time | O(min(n, m)) space
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]