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

# 2nd solution
# Average case: when there aren't too many stings with identical prefixes
# that are found in another string
# O(n * s) time | O(n * s) space
# where n is the number of strings and s is the length of the longest string
def specialStrings(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return list(filter(lambda string: isSpecial(string, trie.root, 0, 0, trie), strings))

def isSpecial(string, trieNode, idx, count, trie):
    char = string[idx]
    if char not in trieNode:
        return False
    
    atEndOfString = idx == len(string) - 1
    if atEndOfString:
        return trie.endSymbol in trieNode[char] and count + 1 >= 2
    
    if trie.endSymbol in trieNode[char]:
        restIsSpecial = isSpecial(string, trie.root, idx + 1, count + 1, trie)
        if restIsSpecial:
            return True
    
    return isSpecial(string, trieNode[char], idx + 1, count, trie)

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {}
            currentTrieNode = currentTrieNode[string[i]]
        currentTrieNode[self.endSymbol] = string