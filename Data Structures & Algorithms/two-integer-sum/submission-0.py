class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in seen:
                if seen[comp] < i:
                    return [seen[comp],i]
                else:
                    return [i, seen[comp]]
            seen[num] = i