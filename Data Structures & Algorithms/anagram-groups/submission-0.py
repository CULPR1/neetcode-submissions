class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = {}
        for s in strs:
            char = [0] * 26
            for i in s:
                char[ord(i) - ord('a')] += 1

            char_tupple = tuple(char)
            if char_tupple not in an_map:
                an_map[char_tupple] = []
            an_map[char_tupple].append(s)



        return list(an_map.values())
                    

        

                    

        