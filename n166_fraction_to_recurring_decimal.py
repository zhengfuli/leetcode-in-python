class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator: return '0'

        if not denominator: return

        sign = 1 if numerator ^ denominator > 0 else 0

        n, d = abs(numerator), abs(denominator)

        res = str(int(n / d))
        if n % d == 0: return res if sign else "-" + res

        res += '.'
        r = n % d
        d = d

        dict = {}

        while r:
            q = str(int((r * 10) / d))

            if r:
                if r not in dict:
                    dict[r] = len(res)
                    res += q
                else:
                    res = res[:dict[r]] + '(' + res[dict[r]:] + ')'
                    break
            r = int((r * 10) % d)
            # print(dict)
        return res if sign else "-" + res
