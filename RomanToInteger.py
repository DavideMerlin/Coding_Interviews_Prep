class Solution:
    def romanToInt(self, s: str) -> int:
        
	    res, prev = 0, 0
      
      #map values 
	    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
      
      #loop from end 
	    for i in s[::-1]:          
		    if dict[i] >= prev:
          #if i is bigger, add to dict
			    res += dict[i] 
                
		    else:
          #otherwise subtract count
			    res -= dict[i]    
        
		    prev = dict[i]
            
	    return res
