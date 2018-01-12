import unittest
class IsValid(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '[':']', '{':'}'}
        left_parentheses = []
        for l in s:
            if l in dict:
                left_parentheses.append(l)
            else:
                if not left_parentheses or l != dict[left_parentheses.pop()]:
                    return False
        return left_parentheses == []

class testBench(unittest.TestCase):
    def setUp(self):
        self.tb = IsValid()

    def testNullInput(self):
        self.assertTrue(self.tb.isValid(""))

    def testNormalInput(self):
        self.assertTrue(self.tb.isValid("()()"))

    def testParenthesesContained(self):
        self.assertTrue(self.tb.isValid("([])({})"))

    def testParenthesesNotCompleted(self):
        self.assertFalse(self.tb.isValid("([]"))

    def testWrongPair(self):
        self.assertFalse(self.tb.isValid("([]{)}"))

if __name__ == '__main__':
    unittest.main()
    # tb = IsValid()
    # print tb.isValid("{()}[]")