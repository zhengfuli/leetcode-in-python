class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1, candidate2 = None, None

        vote1, vote2 = 0, 0

        for num in nums:
            if vote1 <= 0 and num != candidate2:
                candidate1 = num
                vote1 += 1
            elif vote2 <= 0 and num != candidate1:
                candidate2 = num
                vote2 += 1
            else:
                vote1 += 1 if num == candidate1 else -1
                vote2 += 1 if num == candidate2 else -1

                # print(candidate1, candidate2, vote1, vote2)
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1: count1 += 1
            if num == candidate2: count2 += 1

        res = []
        if count1 > len(nums) / 3: res.append(candidate1)
        if count2 > len(nums) / 3 and candidate1 != candidate2: res.append(candidate2)

        return res