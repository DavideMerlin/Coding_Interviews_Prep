class Solution:
    def isValid(self, s: str) -> bool:
    
        #check is even number of brackets
        if len(s)%2 != 0:
            return False
    
        #set of opening brackets
        opening = set('([{') 
    
        #matching Pairs
        matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
        #use a list as a "Stack"
        stack = []
    
        #check every parenthesis in string
        for paren in s:
        
            #if its an opening, append it to list
            if paren in opening:
                stack.append(paren)
        
            else:
            
                #check that there are parentheses in Stack
                if len(stack) == 0:
                    return False
            
                #check the last open parenthesis
                last_open = stack.pop()
            
                #check if it has a closing match
                if (last_open,paren) not in matches:
                    return False
            
        return len(stack) == 0
