class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        length = len(s)

        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for ch in s:
            freqS[ch] += 1
        for ch in t:
            freqT[ch] += 1

        for key, val in freqT.items():
            if freqT[key] > freqS[key]:
                return ""

        if t in s:
            return t

        l = 0
        seen = defaultdict(int)
        temp = ""
        have, need = 0, len(freqT)
        res, resLen = [-1, -1], float("infinity")
        window = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in freqT and window[c] == freqT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] 
            
        
        


            