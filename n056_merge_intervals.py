# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[len(res)-1].start <= interval.start <= res[len(res)-1].end:
                    res[len(res) - 1].end = max(interval.end, res[len(res) - 1].end)
                else:
                    res.append(interval)
        return res
