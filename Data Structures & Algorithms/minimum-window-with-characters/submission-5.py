class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for k in t:
            t_freq[k] = t_freq.get(k,0) + 1

        window = {}
        found = False
        required = len(t_freq)
        formed = 0
        n = len(s)
        result = [0,n-1]
        l = 0
        for r in range(n):
            ch =s[r]
            if ch in t_freq:
                window[ch] = window.get(ch,0) + 1
                if window[ch] == t_freq[ch]:
                    formed += 1

            while l <= r and formed == required:
                found = True
                if r - l + 1 < result[1] - result[0] + 1:
                    result = [l,r]

                left_ch = s[l]
                if left_ch in t_freq:
                    window[left_ch] -= 1
                    if window[left_ch] < t_freq[left_ch]:
                        formed -= 1

                l += 1

        return s[result[0]:result[1] + 1] if found else ""

