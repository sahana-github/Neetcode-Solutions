# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        left=0
        right=len(values)-1
        while left<right:
            if values[left]!=values[right]:
                return False
            left+=1
            right-=1
        return True
        