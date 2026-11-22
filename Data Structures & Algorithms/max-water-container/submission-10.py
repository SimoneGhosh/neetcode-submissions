class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l,r = 0, len(heights)-1

        while l < r:
            w= r-l
            h=min(heights[l], heights[r])
            
            area = max(w*h, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r-=1
        
        return area
