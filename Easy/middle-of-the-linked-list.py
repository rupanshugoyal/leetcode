# https://leetcode.com/problems/middle-of-the-linked-list/


# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = head
        SecondNode = head

        # push firstNode once and SeconedNode twice
        while(SecondNode != None):
            try:
                SecondNode = SecondNode.next.next
            except:
                SecondNode = None
                break
            firstNode = firstNode.next

        return firstNode