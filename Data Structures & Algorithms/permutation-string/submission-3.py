class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map_s1 = {}
        freq_map = {}
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        for l in range(k):
            freq_map_s1[s1[l]] = freq_map_s1.get(s1[l],0) + 1
            freq_map[s2[l]] = freq_map.get(s2[l],0) + 1

        if freq_map == freq_map_s1:
            return True

        for i in range(k,n):
            freq_map[s2[i]] = freq_map.get(s2[i],0) + 1
            freq_map[s2[i - k]] = freq_map.get(s2[i-k],0) - 1
            if freq_map[s2[i - k]] == 0:
                del freq_map[s2[i - k]]
            print(freq_map)
            print(freq_map_s1)
            if freq_map == freq_map_s1:
                return True

        return False
                    


         