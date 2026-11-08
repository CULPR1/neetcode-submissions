class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        prefix = [0] * size
        suffix = [0] * size
        maxed = 0
        for i in range(size):
            if maxed < height[i]:
                maxed = height[i]
            prefix[i] = maxed

        # print(prefix)
        maxed = 0
        for j in range(size - 1,-1,-1):
            if maxed < height[j]:
                maxed = height[j]
            suffix[j] = maxed

        # print(suffix)
        

        water = 0
        for i in range(size):
            water += min(prefix[i],suffix[i]) - height[i]


        return water