class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        res = []

        def dfs(r, c, node):
            char = board[r][c]
            #if char not exist in the Trie
            if char not in node.children:
                return 

            #go to Trie
            node = node.children[char]
            #find word
            if node.word:
                res.append(node.word)
                #not find this word again
                node.word = None
            #mark the visited
            board[r][c] = '#'
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions: 
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < len(board) and 0 <= nc < len(board[0])
                    and board[nr][nc] != '#'
                ):
                    dfs(nr, nc, node)

            board[r][c] = char
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return res