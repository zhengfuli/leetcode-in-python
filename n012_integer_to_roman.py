class IntegerToRoman(object):
    def integerToRoman(self, num):
        symbols = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman = ""
        for i in range(13):

            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]

            if num == 0:
                return roman

        # I=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # X=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # C=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # M=["", "M", "MM", "MMM"]
        # return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
