import unittest

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        dp = [0] * (len(s))

        for i in xrange(len(s)):
            if i == 0 and '1' <= s[i] <= '9':
                dp[i] = 1
            elif i > 0 and s[i - 1] == '0' and '1' <= s[i] <= '9':
                dp[i] = dp[i - 1]
            elif i > 0 and '1' <= s[i - 1] <= '2':
                if s[i] == '0':
                    if i == 1:
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 2]
                elif ('1' == s[i - 1] and '1' <= s[i] <= '9') \
                        or ('2' == s[i - 1] and '1' <= s[i] <= '6'):
                    if i == 1:
                        dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
            elif i > 0 and '3' <= s[i - 1] <= '9' and '1' <= s[i] <= '9':
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0

        # print dp
        return dp[-1]

# class testSolution(unittest.TestCase):
#     def setUp(self):
#         self.tb =Solution()
#
#     def tearDown(self): pass
#
#     def testNull(self):
#         self.assertEqual(self.tb.numDecodings(""), 0)
#
#     def testOneNum(self):
#         self.assertEqual(self.tb.numDecodings("1"), 1)
#
#     def testInvalid(self):
#         self.assertEqual(self.tb.numDecodings("1e12d"), 2)
#
#     def testRepeatNums(self):
#         self.assertEqual(self.tb.numDecodings("1111111"), 21)
#
#     def testComplex(self):
#         self.assertEqual(self.tb.numDecodings("32421431241"), 18)
#
#     def testAllZeros(self):
#         self.assertEqual(self.tb.numDecodings("0000"), 0)
#
#     def testBigNum(self):
#         self.assertEqual(self.tb.numDecodings("27"), 1)
#
# if __name__ == '__main__':
#     unittest.main()

