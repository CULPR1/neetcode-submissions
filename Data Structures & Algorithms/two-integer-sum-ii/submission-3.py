class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr_1 = {}
        for i in range(len(numbers)):
            if numbers[i] not in arr_1:
                arr_1[numbers[i]] = []
            arr_1[numbers[i]].append(i + 1)


        for x in arr_1:
            if target - x == x and len(arr_1[x]) > 1:
                return [arr_1[x][0],arr_1[x][1]]
                
            elif target - x in arr_1:
                return[arr_1[x][0],arr_1[target - x][0]]