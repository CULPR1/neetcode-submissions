class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)
        
        for i in hash_map:
            if target - i not in hash_map:
                continue
            if target - i == i:
                if len(hash_map[i]) >= 2:
                    return [hash_map[i][0],hash_map[target - i][1]]
                else: 
                    continue
            else:
                return [hash_map[i][0],hash_map[target - i][0]]