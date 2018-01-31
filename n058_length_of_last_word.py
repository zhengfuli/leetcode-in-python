class lengthOfLastWord(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip())-1-s.rstrip().rfind(' ')