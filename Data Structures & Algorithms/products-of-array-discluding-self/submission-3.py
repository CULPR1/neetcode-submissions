class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            prefix.append(product)

        nums_flipped = nums[::-1]
        pre_suffix = [1]
        product_2 = 1
        for i in range(len(nums_flipped) - 1):
            product_2 *= nums_flipped[i]
            pre_suffix.append(product_2)
        

        suffix = pre_suffix[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])

        return ans