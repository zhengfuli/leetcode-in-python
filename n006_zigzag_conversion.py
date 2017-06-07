class ZigZagConversion(object):
    def zigzagConversion(self, s, numRows):
        """
        :param s:string 
        :param numRows:int 
        :return:string 
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        string_rows = ['']*numRows
        row, move = 0, 1
        for char in s:
            string_rows[row] += char
            row += move
            if row == numRows-1 or row == 0:
                move = -move
        return ''.join(string_rows)