class Solution:
    def check(self,s : str,start : int,end : int):
        if start >= end:
            return True
        elif start + 1 == end and s[start] == s[end]:
            return True
        elif s[start] == s[end] and self.check(s,start + 1,end - 1):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        string = "".join(x.lower() for x in s if x.isalnum()) 
        size = len(string)
        return self.check(string,0,size - 1)
