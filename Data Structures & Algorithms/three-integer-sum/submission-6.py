class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        size = len(sort_nums)
        result = {}
        for i in range(size - 2):
            if sort_nums[i] > 0:
                break
            target = -sort_nums[i]
            j = i + 1
            k = size - 1
            while(j < k):
                if sort_nums[k] + sort_nums[j] == target:
                    result[tuple([sort_nums[i],sort_nums[j],sort_nums[k]])] = 1
                    k -= 1

                elif sort_nums[j] + sort_nums[k] < target:
                    j += 1

                else:
                    k -= 1

        return list(result)