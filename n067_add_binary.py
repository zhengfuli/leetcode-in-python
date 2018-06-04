class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a: return b
        if not b: return a

        [s, l] = [a, b] if len(a) < len(b) else [b, a]

        s, l = s[::-1], l[::-1]

        carry = 0

        res = ""

        for i in range(len(s)):

            sum = int(s[i]) + int(l[i]) + carry

            residue, carry = int(sum % 2), int(sum / 2)

            res += str(residue)

        for j in range(len(s), len(l)):

            sum = int(l[j]) + carry

            residue, carry = int(sum % 2), int(sum / 2)

            res += str(residue)

        if carry: res += "1"

        return res[::-1]

if __name__ == '__main__':
    tb = Solution()
    print(tb.addBinary("0", "1"))
