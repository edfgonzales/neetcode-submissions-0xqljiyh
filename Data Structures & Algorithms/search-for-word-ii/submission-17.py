class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])

        path, res = set(), set()
        def backtrack(r, c, word, node):
            if (not (0 <= r < ROWS and 0 <= c < COLS) or
                board[r][c] not in node.children or
                (r, c) in path):
                return
            
            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)

            backtrack(r + 1, c, word, node)
            backtrack(r - 1, c, word, node)
            backtrack(r, c + 1, word, node)
            backtrack(r, c - 1, word, node)

            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, "", root)
        return list(res)