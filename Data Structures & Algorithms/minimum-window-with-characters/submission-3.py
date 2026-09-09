class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = {}
        window = {}

        for c in t: 
            countT[c] = countT.get(c, 0) + 1
        
        have = 0 
        need = len(countT)
        res = ""
        resLen = float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need: 
                if (r - l + 1) < resLen:
                    resLen = r - l + 1 
                    res = s[l:r + 1]

                lChar = s[l]
                window[lChar] -= 1

                if lChar in countT and window[lChar] < countT[lChar]:
                    have -= 1
                l += 1

        return res