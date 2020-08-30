# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        extra = 0
        
        while l1 or l2 or extra:
            mysum = 0
            if l1:
                mysum += l1.val
                l1 = l1.next
            if l2:
                mysum += l2.val
                l2 = l2.next
            extra, mysum = divmod(mysum + extra, 10)
            head.next = ListNode(mysum)
            head = head.next
        
        return root.next