class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        curr_sum=0        
        
        for i in range(len(nums)):

            if curr_sum<0:
                curr_sum=0
            curr_sum+=nums[i]
            max_sum=max(max_sum,curr_sum)
            
        return max_sum
            
