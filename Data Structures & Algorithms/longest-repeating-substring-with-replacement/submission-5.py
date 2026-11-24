class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre_map = {}
        l = 0
        k_count = 0
        max_length = 0
        for r in range(len(s)):
            fre_map[s[r]] = fre_map.get(s[r],0) + 1
            most_freq = max(fre_map, key = fre_map.get)
            if s[r] != most_freq:
                k_count += 1

            while r - l + 1 - fre_map[most_freq] > k:
                fre_map[s[l]] -= 1
                l += 1
                most_freq = max(fre_map, key = fre_map.get)

            
            print(l,r)
            length = r -l + 1
            if max_length < length:
                max_length = length


        return max_length
