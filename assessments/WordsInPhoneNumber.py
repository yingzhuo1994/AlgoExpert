# 1st solution
from typing import final


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

# 2nd solution
# O(m * w + n * 3^n) time | O(m * w + n) space
# where n is the length of the phone number,
# m is the number of words,
# and w it the length of the longest word
def wordsInPhoneNumber(phoneNumber, words):
    wordTrie = getWordTrie(words)
    finalWords = {}
    for i in range(len(phoneNumber)):
        exploreTrie(phoneNumber, i, wordTrie.root, finalWords)
    return list(finalWords.keys())

def getWordTrie(words):
    wordTrie = Trie()
    for word in words:
        wordTrie.insert(word)
    return wordTrie

def exploreTrie(phoneNumber, digitIdx, trieNode, finalWords):
    if "*" in trieNode:
        word = trieNode["*"]
        finalWords[word] = True
    
    if digitIdx == len(phoneNumber):
        return 
    
    currentDigit = phoneNumber[digitIdx]
    possibleLetters = DIGIT_LETTERS[currentDigit]
    for letter in possibleLetters:
        if letter not in trieNode:
            continue
        exploreTrie(phoneNumber, digitIdx + 1, trieNode[letter], finalWords)

DIGIT_LETTERS = {
    "0": [],
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def insert(self, word):
        currentTrieNode = self.root
        for letter in word:
            if letter not in currentTrieNode:
                currentTrieNode[letter] = {}
            currentTrieNode = currentTrieNode[letter]
        currentTrieNode[self.endSymbol] = word