# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #set current and previous nodes 
        current = head
        previous = None 
        
        #until we have gone through to the end of the list
        while current:
            
            #copy the current nodes next node to next_node before overwriting as the previous node for reversal
            next_node = current.next
            #reverse the pointer ot the next_node
            current.next = previous
            
            #go one forward in the list
            previous = current 
            current = next_node
            
        return previous 
