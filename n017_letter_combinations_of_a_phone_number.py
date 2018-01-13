class LetterCombinations(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2':'abc', '3':'def', '4':'ghi', \
                '5': 'jkl', '6': 'mno', '7': 'pqrs', \
                '8':'tuv', '9':'wxyz'}
        comb = []

        for bit in digits:
            if bit in dict:
                tmp = []
                for l in dict[bit]:
                    if comb == []:
                        tmp.append(l)
                    for c in comb:
                        tmp.append(c+l)
                comb = tmp
        return comb

if __name__ == '__main__':
    tb = LetterCombinations()
    print tb.letterCombinations("234")