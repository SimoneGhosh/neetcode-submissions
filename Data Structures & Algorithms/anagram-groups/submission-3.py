class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = defaultdict(list)

        for str in strs:
            
            sortstr = ''.join(sorted(str))
            out[sortstr].append(str)
        

        return list(out.values())