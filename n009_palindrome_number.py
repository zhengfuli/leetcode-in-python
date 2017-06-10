class PalindromeNumber(object):
    def palindromeNumber(self, x):
        """
        :param x:int 
        :return:bool
        """
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div *= 10
        while x:
            if x/div != x%10:
                return False
            x %= div
            x /= 10
            div /= 100
        return True