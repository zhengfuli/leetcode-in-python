class ThreeSum(object):
    def threeSum(self, nums):
        counter = {}
        res = []

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        if 0 in counter and counter[0] > 2:
            res.append([0, 0, 0])

        pos = [p for p in counter if p > 0]
        neg = [n for n in counter if n < 0]

        for p in pos:
            for n in neg:
                r = -p - n
                if r in counter:
                    if (r == p or r == n) and counter[r] > 1:
                        res.append([n, r, p])
                    if r < n:
                        res.append([r, n, p])
                    if r > p:
                        res.append([n, p, r])
                    if r == 0:
                        res.append([n, 0, p])

        return res