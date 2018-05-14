class Solution(object):
    def split(self, depth, subsets, start):
        self.res.append(subsets)

        if depth == len(self.nums):
            return

        for i in xrange(start, len(self.nums)):
            self.split(depth+1, subsets+[self.nums[i]], i+1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.nums = nums
        return self.split(0, [], 0)

if __name__ == '__main__':
    tb = Solution()
    tb.subsets([1, 2, 3])
    print tb.res