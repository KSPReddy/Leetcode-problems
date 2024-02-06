# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if None in (list1, list2):
            return list1 or list2
        dummy = current = ListNode(0)
        dummy.next = list1
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            else:
                nxt = current.next
                current.next = list2
                temp = list2.next
                list2.next = nxt
                list2 = temp
            current = current.next
        current.next = list1 or list2
        return dummy.next