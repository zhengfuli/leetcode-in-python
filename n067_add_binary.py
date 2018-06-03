class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        [s , l] = [a, b] if len(a) < len(b) else [b, a]

        carry = 0

        res = ""

        for i in range(-1, -len(s)-1, -1):
            if int(s[i]) and int(l[i]):
                res += "1" if carry else "0"
                carry = 1
            else:
                res += "1" if not carry else "0"
                carry = 0

        for j in range(i, -len(l)-1, -1):
            if int(s[i]) and carry:
                res += "0"
                carry = 1
            else:
                res += "1"
                carry = 0

        print(res)


