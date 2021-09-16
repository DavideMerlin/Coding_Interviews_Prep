class Solution:
    def climbStairs(self, n: int) -> int:
        
        #set variables to 1
        box1 = 1
        box2 = 1
        
        for i in range(n-1):
            
            temp = box1 
            box1 = box1 + box2
            
            #shift two to previous value of one
            box2 = temp
        
        return box1
