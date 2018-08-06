class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        def quick_sort(nums, left, right):
            if left >= right: return nums

            l, r = left, right
            key = nums[l]

            while l < r:
                while l < r and nums[r] >= key:
                    r -= 1

                nums[l], nums[r] = nums[r], nums[l]

                while l < r and nums[l] <= key:
                    l += 1

                nums[r], nums[l] = nums[l], nums[r]

            # print(nums)
            quick_sort(nums, left, l - 1)
            quick_sort(nums, r + 1, right)
            return nums

        if not citations: return 0
        if len(citations) == 1: return min(1, citations[0])

        sorted_citations = quick_sort(citations, 0, len(citations) - 1)
        # print(sorted_citations)

        for i in range(len(sorted_citations) - 1, -1, -1):
            if sorted_citations[i] < len(sorted_citations) - i:
                return len(sorted_citations) - i - 1

        return len(sorted_citations) - i