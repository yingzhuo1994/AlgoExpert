# 1st solution
# O(n) time | O(1) space
def longestSubstringWithoutDuplication(string):
    dic = {}
    start = 0
    ans = ""
    for i, ch in enumerate(string):
        if ch in dic and dic[ch] >= start:
            start = dic[ch] + 1
        dic[ch] = i
        if len(string[start:i+1]) > len(ans):
            ans = string[start:i+1]
    return ans

# 2nd official solution
# O(n) time | O(min(n, a)) space
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]: longest[1]]