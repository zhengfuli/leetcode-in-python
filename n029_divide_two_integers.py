import sys
class Divide(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxint = 2 ** 31 - 1
        divid, divis = int(dividend), int(divisor)

        sign = 1
        if divid < 0:
            divid = abs(divid)
            sign = -sign
        if divis < 0:
            divis = abs(divis)
            sign = -sign

        if divis == 0:
            return 'N/A'

        quotient = 0
        index = 1
        tmp = divis
        while divid >= divis:
            tmp = divis
            index = 1
            while divid >= tmp:
                divid -= tmp
                quotient += index
                tmp <<= 1
                index <<= 1

        if sign > 0:
            quotient = quotient
        else:
            quotient = -quotient

        if quotient < -maxint - 1:
            quotient = -maxint - 1
        if quotient > maxint:
            quotient = maxint

        return quotient
