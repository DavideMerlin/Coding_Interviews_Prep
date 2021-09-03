# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #initialize dummy(starts at the beginnning of the list) and temp (moving of one place) 
        dummy=temp=ListNode(0)
        
        #while l1, l2 are not empty
        while l1 != None and l2 != None:
            
            if l1.val < l2.val:
                #add to list 
                temp.next = l1
                #continue to next l1 node 
                l1 = l1.next 
            else:
                #add to list 
                temp.next = l2
                #continue to next l2 node 
                l2 = l2.next 
            #set temp to next in the list     
            temp = temp.next
            
        #check if they're the same lenght, if not go to end of one of them
        temp.next = l1 or l2
        
        return dummy.next 
