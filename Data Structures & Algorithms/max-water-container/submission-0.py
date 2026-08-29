class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        ans = 0
        while (left < right):
            if heights[left] > heights[right]:
                ans = max(ans, heights[right] * (right - left))
                right = right - 1
            else:
                ans = max(ans, heights[left] * (right - left))
                left = left + 1
        return ans

            
        