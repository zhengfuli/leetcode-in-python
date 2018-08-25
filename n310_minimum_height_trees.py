class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dict = {}

        for edge in edges:
            for node in edge:
                if node not in dict:
                    dict[node] = 1
                else:
                    dict[node] += 1
