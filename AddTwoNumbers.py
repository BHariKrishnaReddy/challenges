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
        if l1 is None and l2 is None:
            return 
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        n1,n2 = l1,l2
        s1,s2="",""
        size = 0
        while n1 is not None:
            s1+=str(n1.value)
            n1 = n1.next
        while n2 is not None:
            s2+=str(n2.value)
            n2 = n2.next
            
        final = [int(i) for i in str( int( str1[::-1] )+int( str2[::-1] ) )[::-1]]
        new_node = l1
        for i in final:
            size+=1
            new_node.val = i
            if new_node.next is None:
                break
            new_node = new_node.next
        diff = len(final)-size
        while len(final)-size>0:
            new_node.next = ListNode(final[size])
            new_node = new_node.next
            size+=1
 
