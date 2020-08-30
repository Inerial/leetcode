# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         tail = None
#         while head:
#             tail, tail.next, head = head, tail, head.next
#         return tail
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            n, node.next = node.next, prev
            prev, node = node, n
        return prev