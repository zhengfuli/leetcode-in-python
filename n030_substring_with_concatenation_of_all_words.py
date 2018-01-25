class FindSubstring(object):
    def findSubstring(self, S, L):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words = {}
        wordNum = len(L)
        for i in L:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
        wordLen = len(L[0])
        res = []
        for i in range(len(S) + 1 - wordLen * wordNum):
            curr = {};
            j = 0
            while j < wordNum:
                word = S[i + j * wordLen:i + j * wordLen + wordLen]
                if word not in words:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > words[word]: break
                j += 1
            if j == wordNum: res.append(i)
        return res

if __name__ == '__main__':
    tb = FindSubstring()
    print tb.findSubstring("cbabcabcabcbacbabbcababcbacbab", ["a", "b", "c"])
