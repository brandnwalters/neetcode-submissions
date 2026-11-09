class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        total = (r - l) * min(heights[l], heights[r])
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > total:
                total = area
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return total


        