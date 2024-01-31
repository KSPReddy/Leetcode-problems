# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        node = slow.next = None
        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp
        first = head
        second = node
        while second:
            temp1,temp2 = first.next,second.next
            first.next,second.next = second,temp1
            first,second = temp1,temp2
        
        