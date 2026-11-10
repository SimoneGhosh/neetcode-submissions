class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped = defaultdict(list)

        for str in strs:
            temp = [0]*26
            for s in str:
                temp[ord(s)-ord('a')] += 1
            grouped[tuple(temp)].append(str)

        return list(grouped.values())
