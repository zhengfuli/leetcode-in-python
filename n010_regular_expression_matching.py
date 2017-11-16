class RegularExpressionMatching(object):
    def regularExpressionMatching(self, s, p):
        check = [(0, 0)]
        added = set([(0,0)])
        s = s[::-1]
        p = p[::-1]
        l1 = len(s)
        l2 = len(p)

        while check:
            p1, p2 = check.pop()

            if p1 == l1 and p2 == l2:
                return True

            if p1 < l1 and p2 < l2 and (s[p1] == p[p2] or p[p2] == '.') and (p1+1, p2+1) not in added:
                check.append((p1+1, p2+1))
                added.append((p1+1, p2+1))

            if p2 < l2 and p[p2] == '*':
                if (p1, p2+2) not in added:
                    check.append((p1, p2+2))
                    added.append((p1, p2+2))
                if p1 < l1 and p2 + 1 < l2 and (s[p1] == p[p2+1] or p[p2+1] == '.') and (p1+1, p2) not in added:
                    check.append((p1+1, p2))
                    added.append((p1+1, p2))

        return False