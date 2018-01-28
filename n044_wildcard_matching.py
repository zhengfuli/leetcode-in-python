class WildCardMatching(object):
    def wildCardMatching(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # sp, and pp are pointers for s and p, star for storing the star position
        # ss for storing the letter in s corresponding to star in p
        sp, pp, star, ss = 0, 0, -1, -1
        while sp < len(s):
            print pp, sp
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
                continue
            if pp < len(p) and p[pp] == '*':
                star, ss = pp, sp
                pp += 1
                continue
            if star != -1:
                pp = star + 1
                ss += 1
                sp = ss
                continue
            return False
        while pp < len(p) and p[pp] == '*':
            pp += 1
        if pp == len(p):
            return True
        return False
