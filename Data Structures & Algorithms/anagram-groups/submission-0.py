class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = []
        vals = {}

        for i, str in enumerate (strs):
            vals[str] = i

        for str in strs:
            copy.append("".join(sorted(str)))

        map = defaultdict(list)
        for i, str in enumerate (copy):
            map[str].append(i)
        
        temp = []
        final = []
        for value in map.values():
            for i in value:
                temp.append(strs[i])
            final.append(temp)
            temp = []
        return final


