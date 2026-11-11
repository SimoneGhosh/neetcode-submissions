class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [0]*len(nums)
        total = 1
        zero = []

        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            
            if nums[i] == 0:
                zero.append(i)
        
        if len(zero) > 1:
            return out
        if len(zero) == 0:
            for i in range(len(nums)):
                out[i] = int(total/nums[i])
        if len(zero) == 1:
            out[zero[0]] = total
        return out
