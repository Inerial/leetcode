# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


## O(n)time, not O(1) space
import time
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        now = time.time()
        
        if head is None:
            return True
        ans = []
        while head.next is not None:
            ans.append(head.val)
            head = head.next
        ans.append(head.val)
        
        print(time.time() - now)
        return ans == list(reversed(ans))


# ## O(n)time, O(1) space인지도 확실하지 않음
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
