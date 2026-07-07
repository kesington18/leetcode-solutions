# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        res = 0
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        newHead = head
        while newHead:
            res += newHead.val * 2 ** (count - 1)
            count -= 1
            newHead = newHead.next
        
        return res