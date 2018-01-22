class RomanToInt(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"M": 1000, "CM": 900, "D": 500,
                "CD": 400, "C": 100, "XC": 90,
                "L": 50, "XL": 40, "X": 10, "IX": 9,
                "V": 5, "IV": 4, "I": 1}
        i, res = 0, 0
        while i + 1 < len(s):
            if s[i:i + 2] in dict:
                res += dict[s[i:i + 2]]
                i += 2
            elif s[i] in dict:
                res += dict[s[i]]
                i += 1
            else:
                return 0
        if i == len(s) - 1 and s[i] in dict:
            res += dict[s[i]]
        return res