'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        out = ListNode(None)
        start = out

        while(l1 is not None or l2 is not None or carry_over != 0):

            if(l1 is not None):
                carry_over += l1.val
                l1 = l1.next
            if(l2 is not None):
                carry_over += l2.val
                l2 = l2.next                
            digit = carry_over % 10
            carry_over //= 10 
            out.val = digit
            out.next = ListNode(None)
            prev = out
            out = out.next
        prev.next = None
        return start
