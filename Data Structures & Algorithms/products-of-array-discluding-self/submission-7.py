class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros == 2:
                    return [0]*len(nums)

            else:
                total = total*num

        if zeros == 0:
            return [total//num for num in nums]

        elif zeros == 1:
            return [0 if num != 0 else total for num in nums] 