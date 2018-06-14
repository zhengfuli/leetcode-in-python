# Definition for a point.
from fractions import Fraction
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length < 3: return length
        max_points = 0
        for i in range(length):
            maps = {'inf':0}
            same = 1
            for j in range(i,length):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    maps['inf'] += 1
                elif points[i].x != points[j].x:
                    k = Fraction(points[i].y-points[j].y, points[i].x-points[j].x)
                    if k not in maps:
                        maps[k] = 1
                    else:
                        maps[k] += 1
                else:
                    same += 1
            max_points = max(max_points,max(maps.values()) + same)
        return max_points
