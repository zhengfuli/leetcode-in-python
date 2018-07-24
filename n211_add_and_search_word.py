import collections
class TreeNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TreeNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for char in word:
            cur_node = cur_node.children[char]
        cur_node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root

        def dfs(word, root):
            cur_node = root
            for i in range(len(word)):
                if word[i] == '.':
                    for node in list(cur_node.children.values()):
                        if dfs(word[i+1:], node): return True
                    return False
                else:
                    cur_node = cur_node.children.get(word[i])
                    if not cur_node:
                        return False

            return cur_node.isWord

        return dfs(word, cur_node)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("abc")
print(obj.search("a.c"))