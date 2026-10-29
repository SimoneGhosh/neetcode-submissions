class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        val = defaultdict(int)
        final = []

        for num in nums:
            val[num] += 1
        
        sort = {k: v for k, v in sorted(val.items(), key=lambda item: item[1], reverse=True)}
        
        mykeys = list(sort.keys())

        for i in range (k):
            final.append(mykeys[i])

        return final