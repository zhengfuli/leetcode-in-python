class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dict = {}

        for edge in edges:
            for i, node in enumerate(edge):
                if node not in dict:
                    dict[node] = [edge[i-1]]
                else:
                    dict[node].append(edge[i-1])

        while len(dict) > 2:
            for key in list(dict.keys()):
                if len(dict[key]) == 1:
                    dict[dict[key][0]].remove(key)
                    del dict[key]

        return len(dict.keys())