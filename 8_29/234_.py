# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if head is None:
#             return True
#         ans = []
#         while head.next is not None:
#             ans.append(head.val)
#             head = head.next
#         ans.append(head.val)
        
#         return ans == list(reversed(ans))in

    
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head is None:
            return True
        ans = deque()
        while head.next is not None:
            ans.append(head.val)
            head = head.next
        ans.append(head.val)
        
        while len(ans) > 1:
            if ans.popleft() != ans.pop():
                return False
        return True
    
    
# ## 중간 reverse부분에서 쓰지도 않은 head가 증발
# import time
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         now = time.time()
        
#         if head is None:
#             return True
        
#         tmp = head
#         tail = None
#         lenth = 0
        
#         while tmp.next:
#             lenth += 1
#             tmp = tmp.next
#         lenth += 1
        
#         temp = head
#         for i in range(lenth):
#             tail, tail.next, temp= temp, tail, temp.next
#             print('temp',temp)
#             print('head',head)
#         print('head',head)
#         print('tail',tail)
#         print('temp',temp)
        
#         for i in range(lenth//2):
#             if head.val != tail.val:
#                 return False
#             head, tail = head.next, tail.next
            
#         print(time.time() - now)
#         return
