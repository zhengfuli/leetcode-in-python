class FindSubstring(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict = {}
        num = len(words)
        length = len(words[0])
        res = []

        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

        # total number of possible combinations of all words
        for i in xrange(len(s)+1-num*length):
            curr = {}
            j = 0
            while j < num:
                word = s[i+j*length:i+(j+1)*length]
                if word not in dict:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > dict[word]:
                    break
                j += 1
            if j == num:
                res.append(i)
        return res

if __name__ == '__main__':
    tb = FindSubstring()
    print tb.findSubstring("cbabcabcabcbacbabbcababcbacbab", ["a", "b", "c"])
