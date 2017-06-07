class LongestPalindromicSubstring(object):
    def longestPalindromicSubstring(self, s):
        """
        :param s:string 
        :return:string
        """
        if s == '':
            return s
        center, edge = 0, 0
        max_radius_center, max_radius = 0, 0,
        preprocessed_s = '#' + '#'.join(s) + '#'
        length = len(preprocessed_s)
        radius = [1]*length
        for i in range(length):
            if i < edge:
                radius[i] = min(radius[2*center-i], edge-i)
            while i-radius[i] >= 0 and i+radius[i] < length and preprocessed_s[i-radius[i]] == preprocessed_s[i+radius[i]]:
                radius[i] += 1
            if i+radius[i] > edge:
                center, edge = i, i+radius[i]
            if radius[i] >= max_radius:
                max_radius_center, max_radius = i, radius[i]
        return s[(max_radius_center-max_radius+1)/2:(max_radius_center+max_radius)/2]