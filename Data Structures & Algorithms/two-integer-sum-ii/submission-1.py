class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l=0
        r=1

        seen = {}

        seen[numbers[l]] = l

        for i in range(len(numbers)-1):
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            else:
                seen[numbers[r]] = r
                val = target-numbers[r]
                if val in seen and seen[val] < r:
                    return[seen[val]+1,r+1]

                r += 1



