class ReverseInteger(object):
    def reverseInteger(self, x):
        """
        :param x:int 
        :return:int 
        """
        MAXINT = 2147483647
        res = int(str(abs(x))[::-1])
        if x >= 0 and res <= MAXINT:
            return res
        elif x < 0 and res <= MAXINT+1:
            return -res
        else:
            return 0