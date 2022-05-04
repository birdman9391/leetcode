# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        cur.next = head

        rotate_step = ((k // length) + 1) * length - k - 1
        for i in range(rotate_step):
            head = head.next
            
        new_head = head.next
        head.next = None
        return new_head
