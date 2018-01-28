class MultiplyStrings(object):
    def multiplyStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        product = [0 for i in xrange(l1 + l2)]
        carry = 0

        for i in xrange(l1):
            for j in xrange(l2):
                product[i + j] += int(num1[::-1][i]) * int(num2[::-1][j])

        for i in xrange(len(product)):
            p = product[i] + carry
            product[i], carry = p % 10, p / 10

        product = product[::-1]
        while product[0] == 0 and len(product) > 1:
            del product[0]

        res = ''
        for i in xrange(0, len(product)):
            res += str(product[i])

        return res