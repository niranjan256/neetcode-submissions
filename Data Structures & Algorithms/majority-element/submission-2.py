class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ME = nums[0]
        count = 0
        for num in nums:
            if ME!=num:
                count-=1
            if count == 0:
                ME = num
            if num == ME:
                count+=1
        return ME
