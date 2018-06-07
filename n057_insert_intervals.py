# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1].start <= interval.start <= res[-1].end:
                    res[-1].end = interval.end if res[-1].end <= interval.end else res[-1].end
                else:
                    res.append(interval)

        return res