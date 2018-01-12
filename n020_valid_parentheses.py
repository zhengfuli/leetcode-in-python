import unittest
class IsValid(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '[':']', '{':'}'}
        left_index = []
        for l in s:
            if l in dict:
                left_index.append(l)
            else:
                if not left_index or l != dict[left_index.pop()]:
                    return False
        return left_index == []

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