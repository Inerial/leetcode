# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



## end를 고정시켜 놓는것이 핵심
## end를 고정시켜놓고 뒤에 있는 것을 앞으로 땡겨오는 방식
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        for _ in range(m-1):
            start  = start.next
        end = start.next
        
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next