class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        dict = {}
        max_len = 0
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += [i]
            else:
                dict[s[i]] = [i]

            if len(dict.keys()) > 2:
                indexes = list(dict.values())
                max_len = max(max_len, max(indexes[0]+indexes[1])-min(indexes[0]+indexes[1])+1)
                dict.pop(list(dict.keys())[0])

        return max_len