import unittest, string
import string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split = str.split(str(s))
        return " ".join(split[::-1])

class TestSolution(unittest.TestCase):
    def test_normal_words(self):
        tb = Solution()
        reversed_words = tb.reverseWords("the sky is blue")
        self.assertEqual(reversed_words, "blue is sky the")

if __name__ == '__main__':
    unittest.main()
