# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge_two(l1, l2):
            new_l = ListNode(0)
            head = new_l
            if l1 and l2:
                while l1 and l2:
                    if l1.val < l2.val:
                        new_l.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        new_l.next = ListNode(l2.val)
                        l2 = l2.next
                    new_l = new_l.next
                    print(new_l.val)

                if l1:
                    while l1:
                        new_l.next = l1
                        new_l = new_l.next
                        l1 = l1.next
                if l2:
                    while l2:
                        print(l2.val)
                        new_l.next = l2
                        new_l = new_l.next
                        l2 = l2.next

                return head.next
            elif l1:
                return l1
            elif l2:
                return l2
            else:
                return None
        
        if len(lists) == 0:
            return None

        temp = lists[0]
        for i in range(1, len(lists)):
            if lists[i] == None:
                continue
            temp = merge_two(lists[i], temp)
                
        return temp

        

                