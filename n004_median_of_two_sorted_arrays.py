class MedianOfTwoSortedArrays(object):
    def medianOfTwoSortedArrays(self, nums1, nums2):
        """
        :param nums1:list[int] 
        :param nums2:list[int] 
        :return:float
        """
        def findKthNum(nums1, nums2, k):
            if len(nums1) > len(nums2):
                return findKthNum(nums2, nums1, k)
            if len(nums1) == 0:
                return float(nums2[k-1])
            if k == 1:
                return min(nums1[0], nums2[0])
            pos1 = min(len(nums1), k/2)
            pos2 = k - pos1
            if nums1[pos1-1] <= nums2[pos2-1]:
                return findKthNum(nums1[pos1:], nums2, pos2)
            else:
                return findKthNum(nums1, nums2[pos2:], pos1)

        if len(nums1) == 0 and len(nums2) == 0:
            return None
        total_length = len(nums1) + len(nums2)
        if total_length%2 == 0:
            k = total_length/2
            return (findKthNum(nums1, nums2, k) + findKthNum(nums1, nums2, k+1))*0.5
        else:
            k = total_length/2 + 1
            return findKthNum(nums1, nums2, k)



