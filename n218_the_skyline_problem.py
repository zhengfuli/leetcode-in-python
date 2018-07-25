class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        cur = 0
        cur_h = -1
        queue = []

        while cur < len(buildings) or queue:
            cur_x = buildings[cur][0] if not queue else queue[-1][1]

            if cur >= len(buildings) or buildings[cur][0] > cur_x:
                while queue and queue[-1][1] <= cur_x: queue.pop()

            else:
                cur_x = buildings[cur][0]
                while cur < len(buildings) and buildings[cur][0] == cur_x