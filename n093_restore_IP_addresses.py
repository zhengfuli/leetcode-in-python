import string
class Solution(object):
    def split(self, s, start, IP, res):
        if start == 3 and s != "":
            if s == str(int(s)) and int(s) <= 255:
                res.append(IP+s)
            return

        for i in xrange(1, 4):
            if i < len(s):
                if s[:i] == str(int(s[:i])) and int(s[:i]) <= 255:
                    self.split(s[i:], start+1, IP+s[:i]+'.', res)


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.split(s, 0, "", res)
        return res

if __name__ == '__main__':
    tb = Solution()
    print tb.restoreIpAddresses("11111111111111111111111111111111111111111111111")