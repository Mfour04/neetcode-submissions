# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        while True:
            node = groupPrev
            for i in range(k):
                node = node.next
                if not node:
                    return dummy.next
        
            groupNext = node.next
            curr = groupPrev.next

            prev = groupNext

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = node 

            groupPrev = temp

