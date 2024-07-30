class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        to_sum=[0]
        for num in nums:
            to_sum.append(to_sum[-1]+num) 
        l_sum=0
        for i in range(len(nums)):
            r_sum=to_sum[-1] - l_sum -nums[i]
            if r_sum==l_sum:
                return i
            l_sum+=nums[i]
        return -1
