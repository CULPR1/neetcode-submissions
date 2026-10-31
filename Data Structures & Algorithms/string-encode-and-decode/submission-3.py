class Solution:

    def encode(self, strs: List[str]) -> str:
            x= ""
            for y in strs:
                length = int(len(y))
                x = x + '.' +  '.' + str(length) + "+" + y

            return x
    def decode(self, s: str) -> List[str]:

        length = int(len(s))
        i = 0
        strs = []
        print(s)
        while(i < length):
            temp_length = ''
            if (s[i] == "."):
                i += 1
                if (s[i] == "."):
                    i += 1
                    while(s[i] != "+"):
                        temp_length = temp_length + s[i]
                        i += 1
                    str_len = int(temp_length) 
                    strs.append(s[i+1:i+ str_len + 1])
            i += 1

        return strs