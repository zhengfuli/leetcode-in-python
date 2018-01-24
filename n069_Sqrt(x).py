class MySqrt(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 1 binary search has similar performance as Newton's in low resolution requirement
        # but it requires special handling when dealing with numbers between 0 and 1
        # if x < 0:
        #     return None
        # if x == 1:
        #     return x
        # left, mid, right = 0, 0, x
        # while mid != (left + right) >> 1:
        #     mid = (left + right) >> 1
        #     if mid ** 2 < x:
        #         left = mid
        #     elif mid**2 == x:
        #         print mid
        #     else:
        #         right = mid
        # return mid
        if x == 1:
            return x
        res = x >> 1
        while res**2 > x:
            res = (res + x / res) >> 1
        return res