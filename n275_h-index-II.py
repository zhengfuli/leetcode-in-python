class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        def binary_search(start, end, hIndex):
            if start > end: return 0

            mid = int((start + end) / 2)
            h = end - mid + 1 + hIndex
            # print(start, end, mid, h)

            if h <= citations[mid]:
                return max(h, binary_search(start, mid - 1, h))
            else:
                return binary_search(mid + 1, end, hIndex)

        return binary_search(0, len(citations) - 1, 0)

tb = Solution()
print(tb.hIndex([7,7,7,7,7,7,7]))