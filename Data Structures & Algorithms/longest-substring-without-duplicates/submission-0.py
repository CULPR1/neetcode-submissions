class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return size
        l = 0
        max_size = 0
        hash_map = set()

        for r in range(size):
            while s[r] in hash_map:
                hash_map.remove(s[l])
                l += 1

            hash_map.add(s[r])

            max_size = max(max_size,r - l + 1)
            
            
        return max_size
        

            


        
            
            
