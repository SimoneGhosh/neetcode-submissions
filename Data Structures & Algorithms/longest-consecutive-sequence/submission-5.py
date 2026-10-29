class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        out = 0
        prev = []
        prev.append(1)

        if len(nums) == 0:
            return 0

        print (nums)
        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] == nums [i+1]-1:
                out += 1
            else:
                prev.append(out+1)
                out = 0
            prev.append(out+1)

        prev.sort(reverse=True)
        print(prev)
        return prev[0]