class LongestSubstringWithoutRepeatingCharacters(object):
    def longestSubstringWithoutRepeatingCharacters(self, s):
        """
        :param s:string 
        :return:int
        """
        max_length = 0
        substring = ''
        for char in s:
            if char in substring:
                substring = substring.split(char)[1]
            substring += char
            if len(substring) > max_length:
                max_length = len(substring)
        return max_length