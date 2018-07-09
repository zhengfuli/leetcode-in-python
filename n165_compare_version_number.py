class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version_nums1, version_nums2 = version1.split("."), version2.split(".")

        while int(version_nums1[-1]) == 0 and len(version_nums1) > 1: version_nums1.pop()
        while int(version_nums2[-1]) == 0 and len(version_nums2) > 1: version_nums2.pop()
        # print(version_nums1, version_nums2)
        len1, len2 = len(version_nums1), len(version_nums2)
        (short, long) = (len1, len2) if len1 <= len2 else (len2, len1)

        for i in range(short):
            if int(version_nums1[i]) > int(version_nums2[i]):
                return 1
            elif int(version_nums1[i]) < int(version_nums2[i]):
                return -1
            else:
                pass

        if len1 == len2:
            return 0
        else:
            return 1 if len2 == short else -1