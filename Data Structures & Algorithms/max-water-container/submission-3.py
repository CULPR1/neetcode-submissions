class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        i = 0
        j = size - 1
        max_vol = 0
        while(i < j):
            temp_vol = (j - i)* min(heights[i],heights[j])
            if max_vol < temp_vol:
                max_vol = temp_vol

            
            if min(heights[i],heights[j]) == heights[i]:
                i += 1

            else:
                j -= 1

        return max_vol