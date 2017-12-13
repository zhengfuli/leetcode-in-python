import unittest
class GenerateParenthesis(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def generate(leftNum, rightNum, s, res):
            if leftNum == 0 and rightNum == 0:
                res.append(s)
            if leftNum > 0:
                generate(leftNum-1, rightNum, s+'(', res)
            if rightNum > 0 and leftNum < rightNum:
                generate(leftNum, rightNum-1, s + ')', res)
        generate(n, n, '', res)
        return res



class testBench(unittest.TestCase):
    def setUp(self):
        self.tb = GenerateParenthesis()

    def tearDown(self):
        pass

    def testNormalInput(self):
        groundTruth = ["((()))",
                       "(()())",
                       "(())()",
                       "()(())",
                       "()()()"]
        self.assertEqual(self.tb.generateParenthesis(3), groundTruth)

    def testNull(self):
        self.assertEqual(self.tb.generateParenthesis(0), [''])

if __name__ == '__main__':
    unittest.main()