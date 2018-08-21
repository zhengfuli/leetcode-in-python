class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        splits = str.split(" ")
        dict = {}

        if len(pattern) != len(splits): return False

        for l in pattern:
            cur = splits.pop(0)

            if l not in dict:
                if cur in list(dict.values()):
                    return False
                else:
                    dict[l] = cur
            else:
                if cur != dict[l]:
                    return False

        return True