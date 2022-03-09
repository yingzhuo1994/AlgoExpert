# 1st solution
def countContainedPermutations(bigString, smallString):
    trie = Trie()
    length = len(smallString)
    for i in range(len(bigString) - length + 1):
        trie.add(bigString, i, length)
    # print(trie.root)
    ans = [0]
    stringList = list(smallString)
    permutationAndCount(stringList, 0, trie, ans)
    return ans[0]

def permutationAndCount(nums, i, trie, ans):
    if i == len(nums) - 1:
        count = trie.contains(nums)
        ans[0] += count
    else:
        for j in range(i, len(nums)):
            swap(nums, i, j)
            permutationAndCount(nums, i + 1, trie, ans)
            swap(nums, i, j)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def add(self, word, startIdx, length):
        dic = self.root
        for i in range(startIdx, startIdx + length):
            if word[i] not in dic:
                dic[word[i]] = {}
            dic = dic[word[i]]
        dic[self.endSymbol] = dic.get(self.endSymbol, 0) + 1
    
    def contains(self, word):
        dic = self.root
        for ch in word:
            if ch not in dic:
                return 0
            dic = dic[ch]
        return dic[self.endSymbol]

# 2nd solution
def countContainedPermutations(bigString, smallString):
    length = len(smallString)
    goalDic = {}
    for ch in smallString:
        goalDic[ch] = goalDic.get(ch, 0) + 1
    curDic = {}
    validCount = 0
    ans = 0
    for i in range(len(bigString)):
        lastIdx = i - length
        if lastIdx >= 0:
            ch = bigString[lastIdx]
            if ch in goalDic and curDic[ch] <= goalDic[ch]:
                validCount -= 1
            curDic[ch] -= 1
        ch = bigString[i]
        if ch in goalDic and curDic.get(ch, 0) < goalDic[ch]:
            validCount += 1
        curDic[ch] = curDic.get(ch, 0) + 1
        if validCount == length:
            ans += 1
    return ans

# 3rd solution
# O(b + s) time | O(s) space
# where b is the length of the big input string
# and s is the length of the small input string
def countContainedPermutations(bigString, smallString):
    smallStringCharCounts = getCharCounts(smallString)
    numUniqueChars = len(smallStringCharCounts.keys())

    runningCharCounts = {}
    permutationsCount = 0
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(bigString):
        rightChar = bigString[rightIdx]
        if rightChar in smallStringCharCounts:
            increaseCharCount(rightChar, runningCharCounts)

            if runningCharCounts[rightChar] == smallStringCharCounts[rightChar]:
                numUniqueCharsDone += 1
        
        if numUniqueCharsDone == numUniqueChars:
            permutationsCount += 1
        
        rightIdx +=1
        shouldIncrementLeftIdx = rightIdx - leftIdx == len(smallString)
        if not shouldIncrementLeftIdx:
            continue

        leftChar = bigString[leftIdx]
        if leftChar in smallStringCharCounts:
            if runningCharCounts[leftChar] == smallStringCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            
            decreaseCharCount(leftChar, runningCharCounts)
        
        leftIdx += 1
    
    return permutationsCount

def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts

def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1

def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1