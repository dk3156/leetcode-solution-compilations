# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == None:
            return False

        hare = head
        turtle = head.next.next

        while hare != None and turtle != None:
            if hare == turtle:
                return True
            try:
                hare = hare.next
                turtle = turtle.next.next
            except:
                return False
            
        return False