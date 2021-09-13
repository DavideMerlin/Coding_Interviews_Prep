class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #reverse array
        digits = digits[::-1]
        track, i = 1, 0
        
        while track:
            #if index is in bpund
            if i < len(digits):
                #special case
                if digits[i] == 9:
                    #reset to 0 when 9 is found 
                    digits[i] = 0
                else:
                    #otherwise, add one and reset
                    digits[i] += 1
                    track = 0
            else:
                #append leftover 1 and reset track
                digits.append(1)
                track = 0
            #increment index    
            i+=1
        #return reversed array    
        return digits[::-1]
