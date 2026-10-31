class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = {}
        for x in nums:
            if x not in array:
                array[x] = 0
            array[x] += 1

        sorted_dict = list(dict(sorted(array.items(),key = lambda item: item[1])))

        return sorted_dict[-1:-1 -k:-1]
        
        


        

        