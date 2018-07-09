class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or not nums: return 0

        mini, maxi = min(nums), max(nums)
        if mini == maxi: return 0

        bucket_gap = int((maxi - mini) / len(nums)) + 1
        bucket_num = int((maxi - mini) / bucket_gap) + 1
        buckets = [[]] * bucket_num

        for num in nums:
            index = int((num - mini) / bucket_gap)
            if not buckets[index]:
                buckets[index] = [num, num]
            else:
                buckets[index][0], buckets[index][1] = min(num, buckets[index][0]), max(num, buckets[index][1])

        max_gap = 0
        pre = 0
        for i in range(1, len(buckets)):
            if buckets[i]:
                max_gap = max(max_gap, buckets[i][0]-buckets[pre][1])
                pre = i

        return max_gap

if __name__ == "__main__":
    tb = Solution()
    print(tb.maximumGap([1, 5, 2, 9]))
