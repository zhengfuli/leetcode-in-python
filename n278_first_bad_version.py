# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def binary_search(start, end):
            if start > end: return n

            mid = int((start + end) / 2)

            if isBadVersion(mid):
                return min(mid, binary_search(start, mid - 1))
            else:
                return binary_search(mid + 1, end)

        return binary_search(0, n)

tb = Solution()
tb.firstBadVersion()