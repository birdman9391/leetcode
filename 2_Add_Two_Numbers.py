# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode()
        ret_cur, l1_cur, l2_cur = ret, l1, l2
        prev_value = 0

        while True:
            ret_cur.val = prev_value
            if l1_cur != None:
                ret_cur.val += l1_cur.val
                l1_cur = l1_cur.next
            if l2_cur != None:
                ret_cur.val += l2_cur.val
                l2_cur = l2_cur.next
            if ret_cur.val >= 10:
                prev_value = 1
                ret_cur.val -= 10
                ret_cur.next = ListNode()
                ret_cur = ret_cur.next
                continue
            else:
                prev_value = 0
                
            if l1_cur == None and l2_cur == None:
                break
            ret_cur.next = ListNode()
            ret_cur = ret_cur.next
            
        return ret