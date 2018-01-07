class LongestCommonPrefix(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if strs:
            for n in xrange(len(strs[0])):
                prefix = strs[0][:n + 1]
                for str in strs[1:]:
                    if str[:n + 1] != prefix:
                        prefix = str[:n]
                        return prefix
            return prefix
        return prefix

if __name__ == '__main__':
    tb = LongestCommonPrefix()
    print tb.longestCommonPrefix([''])



