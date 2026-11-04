class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = defaultdict(list)

        for str in strs:
            
            count = [0]*26
            for s in str:
                count [ord(s)-ord('a')] += 1
            out[tuple(count)].append(str)
        

        return list(out.values())