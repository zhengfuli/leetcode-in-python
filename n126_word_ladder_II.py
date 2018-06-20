class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        start, end, dict = beginWord, endWord, wordList
        if start not in dict: dict.add(start)

        def buildpath(path, word):
            if len(prevMap[word]) == 0:
                path.append(word);
                currPath = path[:]
                currPath.reverse();
                result.add(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()

        result = set([])
        prevMap = {}
        length = len(start)
        for i in dict:
            prevMap[i] = set([])
        candidates = [set(), set()];
        current = 0;
        previous = 1
        candidates[current].add(start)
        while True:
            current, previous = previous, current
            for i in candidates[previous]: dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1 = word[:i];
                    part2 = word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j + part2
                            if nextword in dict:
                                prevMap[nextword].add(word)
                                candidates[current].add(nextword)
            if len(candidates[current]) == 0: return result
            if end in candidates[current]: break
        buildpath([], end)
        return result