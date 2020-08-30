# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         odd = first = ListNode(0)
#         even = second = ListNode(0)
        
#         flag = 0
#         while head:
#             flag += 1
#             if flag % 2 == 0:
#                 second.next = ListNode(head.val)
#                 second = second.next
#             else:
#                 first.next = ListNode(head.val)
#                 first = first.next
#             head = head.next
        
#         first.next = even.next
#         return odd.next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        odd.next = even_head
        return head