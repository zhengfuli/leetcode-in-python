class NextPermutation(object):
    def __init__(self, nums):
        self.nums = nums

    def nextPermutation(self):
        for i in range(len(self.nums)-1, 0, -1):
            if self.nums[i] <= self.nums[i-1]:
                if i == 1:
                    self.nums = self.nums[::-1]
            else:
                for j in range(len(self.nums)-1, i-1, -1):
                    if self.nums[j] > self.nums[i-1]:
                        tmp = self.nums[j]
                        self.nums[j] = self.nums[i-1]
                        self.nums[i-1] = tmp
                self.nums = self.nums[0:i]+self.nums[i:len(self.nums)][::-1]
                break

if __name__ == '__main__':
    nums = [3,2,4,5,2,1]
    tb = NextPermutation(nums)
    print tb.nums
    tb.nextPermutation()
    print tb.nums
