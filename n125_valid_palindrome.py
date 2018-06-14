class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left <= right:

            while left < right and ord(s[left].lower()) not in range(ord("a"), ord("z") + 1) \
                and ord(s[left].lower()) not in range(ord("0"), ord("9") + 1):
                left += 1

            while left < right and ord(s[right].lower()) not in range(ord("a"), ord("z") + 1) \
                and ord(s[right].lower()) not in range(ord("0"), ord("9") + 1):
                right -= 1

            if left > right:
                break

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True