import unittest
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return

        left, right = 0, len(nums)-1

        def dfs(left, right):
            if (right - left) <= 1:
                return min(nums[left], nums[right])

            mid = int((left + right) / 2)

            if nums[mid] == nums[right] and nums[mid] == nums[left]:
                return dfs(left+1, right)

            elif nums[mid] < nums[left] or nums[left] < nums[mid] <= nums[right]:
                return dfs(left, mid)

            else:
                return dfs(mid, right)

        return dfs(left, right)

class TestFindMin(unittest.TestCase):
    def testEarlyPivot(self):
        tb = Solution()
        self.assertEqual(tb.findMin([4, 0, 4, 4, 4]), 0)

    def testLatePivot(self):
        tb = Solution()
        self.assertEqual(tb.findMin([4, 5, 6, 6, 7, 3, 3]), 3)

    def testEvenNumberElements(self):
        tb = Solution()
        self.assertEqual(tb.findMin([3, 3, 1, 3]), 1)

    def testNullList(self):
        tb = Solution()
        self.assertEqual(tb.findMin([]), None)

    def testShortList(self):
        tb = Solution()
        self.assertEqual(tb.findMin([1]), 1)
        self.assertEqual(tb.findMin([1, 1]), 1)

    def testNotRoatated(self):
        tb = Solution()
        self.assertEqual(tb.findMin([1, 3, 3]), 1)

if __name__ == "__main__":
    unittest.main()
