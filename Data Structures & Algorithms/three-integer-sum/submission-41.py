class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        total = 0

        nums.sort()

        for i in range (len(nums)):
            if nums[i] > 0:
                break
            
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            l, r = i+1, len(nums)-1
            while (l<r):
                total = nums[i] + nums[l] + nums[r]

                if total > 0 and l < r:
                    r -= 1
                elif total < 0 and l < r:
                    l += 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return out