class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # Find how many numbers (tiles) there are
        expected_sum = n * (n + 1) // 2  # Calculate the total sum if none were missing
        actual_sum = sum(nums)  # Calculate the sum of the numbers we still have
        return expected_sum - actual_sum  # The missing number is the difference
        
