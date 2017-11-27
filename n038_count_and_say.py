class CountAndSay(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
        else:
            preSay = self.countAndSay(n - 1)
            say, tmp, count, = '', preSay[0], 0
            for char in preSay:
                if char == tmp:
                    count += 1
                else:
                    say += str(count) + tmp
                    tmp, count = char, 1
            say += str(count) + tmp
        return say
# if __name__ == '__main__':
#     test = CountAndSay()
#     test.countAndSay(3)
