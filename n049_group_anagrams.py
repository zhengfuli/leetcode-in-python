class GroupAnagrams(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for str in strs:
            index = tuple(sorted([l for l in str]))
            if index in dict:
                dict[index].append(str)
            else:
                dict[index] = [str]
        return [dict[key] for key in dict.keys()]
