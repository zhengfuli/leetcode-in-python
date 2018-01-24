class StrStr(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # string.find()
        if not needle:
            return 0
        if not haystack:
            return -1
        l = len(needle)
        for c in xrange(0, len(haystack)):
            if haystack[c:c+l] == needle:
                return c
        return -1