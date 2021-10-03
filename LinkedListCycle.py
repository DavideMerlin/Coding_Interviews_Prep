# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        #begin both markers at the first node
        marker1 = head
        marker2 = head

        #go until end of list
        while marker2 != None and marker2.next != None:
        
            marker1 = marker1.next
            #move marker2 ahead
            marker2 = marker2.next.next

        #check if the markers have matched
            if marker2 == marker1:
                return True

        #case where marker ahead reaches the end of the list
        return False
