class CombinationSum(object):
    def dfs(self, candidates, target, start, comb, sol):
        if target == 0:
            return sol.append(comb)
        for i in xrange(start, len(candidates)):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i, comb + [candidates[i]], sol)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        sol = []
        if target <= 0:
            return []
        self.dfs(candidates, target, 0, [], sol)
        return sol