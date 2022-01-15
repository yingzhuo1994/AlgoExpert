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