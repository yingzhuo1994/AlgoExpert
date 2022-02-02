# 1st solution
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)

    length = [len(words)]    
    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, i, j, trie.root, "", result, length)

    return result

def dfs(board, i, j, node, path, result, length):
    if length[0] == 0:
        return

    if node.end:
        print("find it:", path)
        result.append(path)
        length[0] -= 1
        node.end = False
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != "###":           
        temp = board[i][j]
        if temp not in node.dic:
            return 
        board[i][j] = "###"
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if (x, y) != (0, 0):
                    row, col = i + x, j + y    
                    dfs(board, row, col, node.dic[temp], path + temp, result, length)
        board[i][j] = temp

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for ch in word:
            node = node.dic.setdefault(ch, TrieNode())
        node.end = True

    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.dic:
                print(word, node.end)
                return 
            node = node.dic[ch]
        print(word, node.end)
                    
class TrieNode:
    def __init__(self):
        self.dic = {}
        self.end = False

# 2nd solution
# O(nm*8^s + ws) time | O(nm + ws) space
def boggleBoard(board, words):
	trie = Trie()
	for word in words:
		trie.add(word)
	finalWords = {}
	visited = [[False for letter in row] for row in board]
	for i in range(len(board)):
		for j in range(len(board[i])):
			explore(i, j, board, trie.root, visited, finalWords)
	return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
	if visited[i][j]:
		return
	letter = board[i][j]
	if letter not in trieNode:
		return 
	visited[i][j] = True
	trieNode = trieNode[letter]
	if "*" in trieNode:
		finalWords[trieNode["*"]] = True
	neighbors = getNeighbors(i, j, board)
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
	visited[i][j] = False

def getNeighbors(i, j, board):
	neighbors = []
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			if (x, y) != (0, 0):
				row, col = i + x, j + y
				if 0 <= row and row < len(board) and 0 <= col and col < len(board[0]):
					neighbors.append([row, col])
	return neighbors

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
	
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = word