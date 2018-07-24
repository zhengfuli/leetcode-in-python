import collections
class TreeNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TreeNode)
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TreeNode()

    def add(self, word):
        cur_node = self.root
        for char in word:
            cur_node = cur_node.children[char]
        cur_node.isWord = True

    def search(self, word):
        cur_node = self.root
        for char in word:
            cur_node = cur_node.children.get(char)
            if not cur_node:
                return False
        return cur_node.isWord

    def isPrefix(self, word):
        cur_node = self.root
        for char in word:
            cur_node = cur_node.children.get(char)
            if not cur_node:
                return False
        return True

class Solution:
    def __init__(self):
        self.trie = Trie()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for word in words:
            self.trie.add(word)

        visited = [[False]*len(board[0]) for i in range(len(board))]

        res = []

        def dfs(word, x, y):
            if not self.trie.isPrefix(word+board[x][y]):
                return
            else:
                if self.trie.search(word+board[x][y]):
                    res.append(word+board[x][y])
                    visited

                for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if


