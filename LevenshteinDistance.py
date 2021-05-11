def levenshteinDistance(str1, str2):
    # Write your code here.
    print(str1, str2)
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

print(levenshteinDistance("abcdefghij", "1234567890"))
