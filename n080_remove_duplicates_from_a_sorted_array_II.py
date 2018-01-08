import unittest
class RemoveDuplicatesII(object):
    def removeDuplicatesII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-2:
            while i < len(nums)-2 and nums[i] == nums[i+2]:
                nums.remove(nums[i+2])
            i += 1
        return nums


class testBench(unittest.TestCase):
    def setUp(self):
        self.tb = RemoveDuplicatesII()

    def testNormalInput(self):
        self.assertEqual(self.tb.removeDuplicatesII([1,1,1,2,2,3]), [1,1,2,2,3])

    def testComplexInput(self):
        self.assertEqual(self.tb.removeDuplicatesII([1,1,1,1,2,2,2,3]), [1,1,2,2,3])

    def testNoChange(self):
        self.assertEqual(self.tb.removeDuplicatesII([1,2,3]), [1,2,3])

    def testSingleInput(self):
        self.assertEqual(self.tb.removeDuplicatesII([1,1,1]), [1,1])

    def testNullInput(self):
        self.assertEqual(self.tb.removeDuplicatesII([]), [])

if __name__ == '__main__':
    unittest.main()