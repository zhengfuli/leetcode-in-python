class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10: return []

        dict = {}
        for i in range(len(s) - 9):
            dict[s[i:i + 10]] = 1 if s[i:i + 10] not in dict else dict[s[i:i + 10]] + 1

        res = []
        for key in dict.keys():
            if dict[key] >= 2:
                res.append(key)

        return res