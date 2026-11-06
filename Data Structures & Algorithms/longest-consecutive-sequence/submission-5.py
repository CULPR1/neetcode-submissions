class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_num = sorted(set(nums))
        size = len(sort_num)
        print(sort_num)
        i = 0
        j = 1
        length = 1
        if size == 0:
            return 0
        while(i < size and j < size):
            if sort_num[i] + 1 != sort_num[j]:
                i += 1
                j += 1
            else:
                while(j + 1 < size and sort_num[j] + 1 == sort_num[j + 1]):
                    j += 1
                if length < j - i + 1:
                    length = j - i + 1
                i = j
                j = i + 1

        return length