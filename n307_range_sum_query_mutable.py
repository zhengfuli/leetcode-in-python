class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums)
        self.sub_sum = [sum(nums[:i + 1]) for i in range(self.length)]
        self.sub_sum_inverse = [sum(nums[i:]) for i in range(self.length)]
        self.total_sum = sum(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        for j in range(i, self.length):
            self.sub_sum[j] += val - self.nums[i]

        for k in range(i + 1):
            self.sub_sum_inverse[k] += val - self.nums[i]

        self.total_sum += val - self.nums[i]
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # print(self.sub_sum, self.sub_sum_inverse)
        return self.sub_sum[j] + self.sub_sum_inverse[i] - self.total_sum



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)