class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        rest = 0

        if sum(gas) < sum(cost): return -1

        for i in range(len(gas)):
            if rest + gas[i] < cost[i]:
                start = i + 1
                rest = 0
            else:
                rest += gas[i] - cost[i]

        return start