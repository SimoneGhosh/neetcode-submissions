class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringLen = 1
        newLen = 0
        lengths = []

        length = len(s)-1

        seen = []

        left = 0
        right = 1

        if len(s) == 0:
            return 0
        if len(s)==1:
            return 1

        seen.append(s[left])
        while right <= length:
            if s[left] != s[right] and not s[right] in seen:
                substringLen += 1
                seen.append(s[right])
                right += 1
                lengths.append(substringLen)
                print (s[left:right], " ", substringLen)
                
            else:
                newLen += 1
                left += 1
                right = left+1
                print(s[left:right] + " " , newLen)

                lengths.append(substringLen)
                substringLen = newLen
                
                newLen = 0
                seen.clear()
            
        lengths.sort()

        return lengths[-1]
            

