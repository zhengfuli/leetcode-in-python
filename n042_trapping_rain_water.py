class TrappingRainWater(object):
    def trappingRainWater(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax = 0
        leftMaxHeight = []
        for i in xrange(len(height)):
            leftMax = max(leftMax, height[i])
            leftMaxHeight.append(leftMax)

        rightMax = 0
        vol = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax = max(rightMax, height[i])
            if min(leftMaxHeight[i], rightMax) > height[i]:
                vol += min(leftMaxHeight[i], rightMax) - height[i]

        return vol
