# 1st solution
# O(nm * min(n, m)) time | O(nm * min(n, m)) space
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len)
    return lcs[-1][-1]

# 2nd solution
# O(nm*min(n, m)) time | O((min(n, m)^2)) space
def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenLcs = [[] for x in range(len(small) + 1)]
    oddLcs = [[] for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentLcs = oddLcs
            previousLcs = evenLcs
        else:
            currentLcs = evenLcs
            previousLcs = oddLcs
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j -1]:
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
            else:
                currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len)
    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]
    