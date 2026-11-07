class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = []
        for i in range(size - 2):
            if nums[i] > 0:
                return result
            target = -nums[i]
            j = i + 1
            k = size - 1
            while(j < k):
                two_sum = nums[j] + nums[k]
                if two_sum == target and [nums[i],nums[j],nums[k]] not in result:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                elif two_sum < target:
                    j += 1

                else:
                    k -= 1

        return result