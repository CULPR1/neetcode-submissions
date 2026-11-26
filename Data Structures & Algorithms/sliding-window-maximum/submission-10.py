class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heapped = [(-nums[i],i) for i in range(k)]


        heapq.heapify(heapped)
        max_value = [-heapped[0][0]]
        for i in range(k,n):
            heapq.heappush(heapped,(-nums[i],i))
            while heapped[0][1] <= i - k:
                heapq.heappop(heapped)

            
            max_value.append(-heapped[0][0])

        return max_value
