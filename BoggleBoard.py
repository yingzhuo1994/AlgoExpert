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