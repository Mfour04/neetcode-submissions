class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            
            char = word[i]
            if char != ".":
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

            for child in node.children.values():
                if dfs(child, i + 1):
                    return True

            return False
        return dfs(self.root, 0)
