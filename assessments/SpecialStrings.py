# 1st solution
# O(n * 2^s) time | O(n) space 
# where n is the number of strings and s is the length of the longest string
def specialStrings(strings):
    dic = {}
    for string in strings:
        if len(string) not in dic:
            dic[len(string)] = set()
        dic[len(string)].add(string)
    
    ans = []
    for i in range(len(strings)):
        dfs(strings[i], dic, ans, 0, 0, "")
    return ans

def dfs(string, dic, ans, idx, count, cur):
    if string == cur and count > 1:
        ans.append(string)
        return True
    if idx > len(string):
        return False
    for i in range(idx + 1, len(string) + 1):
        length = i - idx
        partString = string[idx:i]
        if length in dic and partString in dic[length]:
            if dfs(string, dic, ans, i, count + 1, cur + partString):
                return True
    return False