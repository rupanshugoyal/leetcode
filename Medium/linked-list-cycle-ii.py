# https://leetcode.com/problems/linked-list-cycle-ii/

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        oneStepPtr = head
        twoStepPtr = head
        if head.next != None and head.next.next != None:
            oneStepPtr = head.next
            twoStepPtr = head.next.next
        else:
            return None

        while oneStepPtr != twoStepPtr:
            if oneStepPtr == twoStepPtr:
                break
            try:
                oneStepPtr = oneStepPtr.next
                twoStepPtr = twoStepPtr.next.next
            except:
                return None

        oneStepPtr = head
        while oneStepPtr != twoStepPtr:
            oneStepPtr = oneStepPtr.next
            twoStepPtr = twoStepPtr.next
        
        return oneStepPtr