# 1st solution
def wordsInPhoneNumber(phoneNumber, words):
    trie = Trie()
    for i in range(len(phoneNumber)):
        trie.add(phoneNumber[i:])
    keypad = {
        "a": "2", "b": "2", "c": "2",
        "d": "3", "e": "3", "f": "3",
        "g": "4", "h": "4", "i": "4",
        "j": "5", "k": "5", "l": "5",
        "m": "6", "n": "6", "o": "6",
        "p": "7", "q": "7", "r": "7", "s": "7",
        "t": "8", "u": "8", "v": "8",
        "w": "9", "x": "9", "y": "9", "z": "9",
    }
    ans = []
    for word in words:
        dic = trie.root
        isContained = True
        for ch in word:
            key = keypad[ch]
            if key not in dic:
                isContained = False
                break
            dic = dic[key]
        if isContained:
            ans.append(word)
    return ans
                 
class Trie:
    def __init__(self):
        self.root = {}
        self.end = "end"
    
    def add(self, word):
        dic = self.root
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = True