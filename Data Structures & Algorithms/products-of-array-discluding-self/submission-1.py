class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range (len(nums)):
            output.append(1)

        for i, val in enumerate (output):
            for j, num in enumerate (nums):
                if i != j:
                    output[i] = output[i]*num
                    print(output[i])
        
        return output