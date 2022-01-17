# 1st solution
def multiStringSearch(bigString, smallStrings):
    stack = bigString.split()
    trie = Trie()
    for word in stack:
        trie.repeatAdd(word)
    ans = []
    for word in smallStrings:
        ans.append(trie.isContained(word))
    return ans

class Trie:
    def __init__(self):
        self.dic = {}
    
    def repeatAdd(self, word):
        for i in range(len(word)):
            self.add(word, i)

    def add(self, word, idx):
        dic = self.dic
        for i in range(idx, len(word)):
            ch = word[i]
            if ch not in dic:
                dic[ch] = {}
            dic = dic.get(ch, {})
    
    def isContained(self, word):
        dic = self.dic
        for ch in word:
            if ch not in dic:
                return False
            dic = dic[ch]
        return True