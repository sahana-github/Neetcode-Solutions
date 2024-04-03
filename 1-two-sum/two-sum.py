class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices={}
        for i,num in enumerate(nums):
            difference=target-num
            if difference in num_indices:
                return [num_indices[difference],i]
            num_indices[num]=i
        
# we have to find difference between list and target
#enumarate will give u corresponding indices along with the list data
# first we find the difference from list and target 
# and store in num_indices in form of {num:indices}
# second step we do same we find diffrence with target and 2nd number in list
# then we check if the difference output is present in num_indices{}  if yes then we return both the indices

# Example
#nums = [2,7,11,15], target = 9
#1st iteration:
#num_indices={}
#i=0,num=2
# difference=7 -->(9-2=7)
# num_indices={2:0}
#2nd iteration:
#i=1,num=7
# difference=2 -->(9-7=2)
# num_indices[2]=0
# return [0,1]