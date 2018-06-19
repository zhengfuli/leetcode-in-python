class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        wordList = set(wordList)
        while queue:
            word, length = queue.pop(0)

            if word == endWord:
                return length

            for i in range(len(word)):
                for letter in "qwertyuiopasdfghjklzxcvbnm":
                    if word[i] != letter:
                        nextWord = word[:i] + letter + word[i+1:]
                        if nextWord in wordList:
                            queue.append((nextWord, length + 1))
                            wordList.remove(nextWord)

        return 0
