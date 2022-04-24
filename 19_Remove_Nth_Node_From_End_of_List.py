#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        myList = []
        cur = head
        while cur is not None:
            myList.append(cur)
            cur = cur.next
        
        if len(myList) == n:
            head = head.next
        else:
            myList[len(myList) - n -1].next = myList[len(myList) - n + 1] if n != 1 else None
        return head
        