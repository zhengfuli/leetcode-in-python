class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t): return False
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))