class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t): return False

        dict = {}
        for c in s:
            dict[c] = 1 if c not in dict else dict[c] + 1

        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1

        for i in list(dict.values()):
            if i: return False

        return True


