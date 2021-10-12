class Solution:
    def reverseBits(self, n: int) -> int:
        #set output 
        output = 0 
        
        for i in range(32):
            #get ith bit of n
            bit = (n >> i) & 1
            #logic or 
            output = output | (bit << (31 - i))
            
        return output
