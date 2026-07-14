"""
Note that we are trying to compute the max are of a rectangle.
area = width x height
height = min(hBar1, hBar2)
widht = Bar2Idx - Bar1Idx

How do we get the max?
The bruteforce way to do this is by trying every bar. We start from one bar 
on the left, and compute every area as we shift the right bar by one to the right
Time: O(N^2) where N is the number of input in heights

The key insights: Ideally we'd want two of the tallest bars with the most distance
This is my thought process:
- Imagine we are starting with a bar on the left with height of hleft
- Now, as we move to the right, we will find bars that are 1) shorter, 2) same height or 3) taller than hleft
- If it is shorter and/or same height, let's call this hright, we know that they
  anchor for the height is hright and the width the the distance. We can compute them and store them if they are bigger
  than what we have computed so far 
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            max_area = max(max_area, width * height)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1

        return max_area