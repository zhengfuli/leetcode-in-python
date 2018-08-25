class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 2: return [0]

        dict = {}

        for edge in edges:
            for i, node in enumerate(edge):
                if node not in dict:
                    dict[node] = [edge[i - 1]]
                else:
                    dict[node].append(edge[i - 1])
        # print(dict)
        while len(dict) > 2:
            leaf = []
            for key in list(dict.keys()):
                if len(dict[key]) == 1:
                    leaf.append([key, dict[key][0]])

            for pair in leaf:
                dict[pair[1]].remove(pair[0])
                del dict[pair[0]]

        return list(dict.keys())