class ContainerWithMostWater(object):
    def containerWithMostWater(self, height):
        p1, p2, volume, maxVolume = 0, len(height) - 1, 0, 0
        while p1 <= p2:
            if height[p1] < height[p2]:
                volume = height[p1] * (p2 - p1)
                p1 += 1
            else:
                volume = height[p2] * (p2 - p1)
                p2 -= 1
            if volume > maxVolume:
                maxVolume = volume
        return maxVolume
