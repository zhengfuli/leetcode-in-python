class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin = list('{:032b}'.format(n))
        reversed = bin[::-1]
        res = int(''.join(reversed),2)
        return res