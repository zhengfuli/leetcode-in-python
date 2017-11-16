class PalindromeNumber(object):
    def palindromeNumber(self, x):
        """
        :param x:int 
        :return:bool
        """
        return str(x) == str(x)[::-1]