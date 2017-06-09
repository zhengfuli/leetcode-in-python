class StringToInteger(object):
    def stringToInteger(self, str):
        """
        :param str:string 
        :return:int 
        """
        MAXINT = 2147483647
        sign, res = 0, 0
        for char in str.lstrip():
            if '0' <= char <= '9':
                res = res*10 + ord(char) - 48
            elif sign == 0 and char == '+':
                sign = 1
            elif sign == 0 and char == '-':
                sign = -1
            else:
                break
        if sign == -1:
            res = -res
        if res > MAXINT:
            return MAXINT
        elif res < -MAXINT-1:
            return -MAXINT-1
        else:
            return res
