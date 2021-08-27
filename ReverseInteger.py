class Solution:
    def reverse(self, x: int) -> int:
        
        #get absolute value of x, strip and reverse it
        n = str(abs(x))
        n = n.strip()
        n = n[::-1]
        
        #store results in output as int
        output = int(n)
        
        #costrains
        if output >= 2** 31 -1 or output <= -2** 31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output
