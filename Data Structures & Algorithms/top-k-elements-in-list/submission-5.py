class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num - freq

        temp = {}
        for num in nums:
            temp[num] = 1 + temp.get(num, 0)
        
        # freq - list of num
        sort = [[] for i in range(len(nums) + 1)]
        for key, val in temp.items():
            sort[val].append(key)

        # return top k
        final = []
        for i in range (len(sort)-1, 0, -1):
            for num in sort[i]:
                final.append(num)
                k = k-1
                if k == 0:
                    return final