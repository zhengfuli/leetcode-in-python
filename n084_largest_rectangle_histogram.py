class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        maxArea = 0

        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                last_index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, width * heights[last_index])
                i -= 1
            i += 1

        while stack:
            last_index = stack.pop()
            width = i if not stack else len(heights) - stack[-1] - 1
            maxArea = max(maxArea, width * heights[last_index])
        return maxArea
