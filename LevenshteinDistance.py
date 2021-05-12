from typing import Counter


def levenshteinDistance(str1, str2):
    # Write your code here.
    # 1st recursive solution
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
    table = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for j in range(1, len(str2) + 1):
        table[0][j] = j
    for i in range(1, len(str1) + 1):
        table[i][0] = i
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cur = min(table[i-1][j], table[i][j-1], table[i-1][j-1])
            if str1[i-1] == str2[j-1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = cur + 1
    return table[-1][-1]

