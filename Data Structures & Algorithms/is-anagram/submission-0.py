class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_map = {}
        for k in s:
            if k in check_map:
                check_map[k] += 1
            else:
                check_map[k] = 1

        for l in t:
            if l in check_map:
                check_map[l] -= 1
            else:
                return False
        
        for k in check_map:
            if check_map[k] != 0:
                return False

        return True