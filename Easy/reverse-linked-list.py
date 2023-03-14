# https://leetcode.com/problems/reverse-linked-list

# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        reverseLinkedList = None
        tempNode = None

        while (head != None):
            # extract one node from starting in temporary node
            tempNode = head
            head = head.next

            # add one node in reverse list.
            tempNode.next = reverseLinkedList
            reverseLinkedList = tempNode

        return reverseLinkedList
