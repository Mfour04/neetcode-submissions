class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAreas = 0
        heights.append(0)
        for  i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                width = i  if not stack else i - stack[-1] - 1
                maxAreas = max(maxAreas, height * width)

            stack.append(i)
        return maxAreas