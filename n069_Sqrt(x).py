class MySqrt(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = 0.0
        mid = 0.0
        max = num*1.0

        while (max-min) > 0.0000001:
            mid = (min+max)/2.0
            if mid*mid >= num:
                max = mid
            else:
                min = mid
        return mid