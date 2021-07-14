from typing import List


class WaterContainer:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height)
        max_vol = 0

        left, right = 0, n - 1

        while left + 1 < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > max_vol:
                max_vol = vol
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        # post
        max_vol = max(max_vol, min(height[left], height[right]) * (right - left))
        return max_vol
