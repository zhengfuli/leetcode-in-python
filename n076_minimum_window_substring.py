class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        keys = set([])
        for char in s + t:
            keys.add(char)
        keys = list(keys)

        target_dict, source_dict = {}, {}
        for key in keys:
            target_dict[key], source_dict[key] = 0, 0

        for char in t:
            target_dict[char] += 1

        print(target_dict, source_dict)

        found = 0
        min_start, min_end, min_len, substring_start = -1, -1, len(s), 0
        for i in range(len(s)):

            source_dict[s[i]] += 1

            if source_dict[s[i]] <= target_dict[s[i]] and source_dict[s[i]] != 0: found += 1

            if found == len(t):
                while substring_start < i and source_dict[s[substring_start]] > target_dict[s[substring_start]]:
                    source_dict[s[substring_start]] -= 1
                    substring_start += 1

                if i - substring_start < min_len:
                    min_start, min_end = substring_start, i
                    min_len = min_end - min_start

                source_dict[s[substring_start]] -= 1
                substring_start += 1
                found -= 1

        if min_start == -1:
            return ""
        else:
            return s[min_start:min_end + 1]









