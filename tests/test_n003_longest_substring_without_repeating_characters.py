import unittest
from n003_longest_substring_without_repeating_characters import LongestSubstringWithoutRepeatingCharacters

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.dut = LongestSubstringWithoutRepeatingCharacters()

    def testNoRepeatingCharacters(self):
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters(''), 0)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('a'), 1)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('  a'), 2)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('abcde'), 5)

    def testContainRepeatingCharacters(self):
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('aaaaaaa'), 1)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('abcdbca'), 4)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('abbba'), 2)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('aabb'), 2)
        self.assertEqual(self.dut.longestSubstringWithoutRepeatingCharacters('aab'), 2)