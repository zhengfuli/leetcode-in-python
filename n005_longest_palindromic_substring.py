class LongestPalindromicSubstring(object):
    def longestPalindromicSubstring(self, s):
        """
        :param s:string 
        :return:string
        """
        center, edge, max_radius, substring_center = 0, 0, 0, 0
        string = '#' + '#'.join(s) + '#'
        radius = [1 for i in range(len(string))]
        for i in range(len(string)):
            if i < edge:
                radius[i] = min(radius[2*center-i], edge-i)
            while i-radius[i] >= 0 and i+radius[i] < len(string) and string[i-radius[i]] == string[i+radius[i]]:
                radius[i] += 1
            if i+radius[i] > edge:
                edge = i + radius[i]
                center = i
            if radius[i] >= max_radius:
                max_radius = radius[i]
                substring_center = i
        return string[substring_center-max_radius+2:substring_center+max_radius-1].replace('#','')