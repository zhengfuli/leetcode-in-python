class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.total_sum = sum(nums)
        self.sub_sum = [sum(nums[:i]) for i in range(1, len(nums) + 1)]
        self.sub_sum_inverse = [sum(nums[i:]) for i in range(len(nums))]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sub_sum_inverse[i] + self.sub_sum[j] - self.total_sum


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)