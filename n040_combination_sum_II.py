class CombinationSum2(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, start, comb, sol):
            if target == 0:
                return sol.add(comb)
            for i in xrange(start, len(candidates)):
                if target < candidates[i]:
                    return
                dfs(candidates, target - candidates[i], i + 1, comb + tuple([candidates[i]]), sol)

        candidates.sort()
        sol = set()
        dfs(candidates, target, 0, (), sol)
        return [list(s) for s in sol]